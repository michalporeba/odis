from typing import Dict
from django.http import  HttpResponseBadRequest, Http404, HttpResponse
from django.shortcuts import render
from http import HTTPStatus
from rest_framework.views import APIView
from rest_framework.response import Response
from .wstl import Wstl, WstlClient
from .wstl_django import DjangoWstlContext
from .models import Connection, Organisation, Service, Membership
from django_kinder_settings import settings
from .apps import Odis
from .serializers import OrganisationSerlializer, ServiceSerializer, ConnectionSerializer, MembershipSerializer
import json

class HttpResponseBadTransition(HttpResponse):
    status_code = 409


class Hello(APIView):
    def get(self, request):
        wstl = Wstl("ODIS - Hello")
        wstl = wstl.with_get_action("self", "odis-home")
        wstl = wstl.with_get_action("home", "odis-home")
        wstl = wstl.with_get_action("node", "odis-node")
        wstl = wstl.with_get_action("alps", "odis-alps")
        wstl = wstl.with_get_action("odis:service", "odis-service")
        wstl = wstl.with_get_action("odis:owner", "odis-node-owner")
        return Response(wstl.to_data())


class Client(APIView):
    def get(self, request):
        client = WstlClient("http://127.0.0.1:8001/odis/")
        return Response(client.hello().to_data())


class Node(APIView):
    def get(self, request):
        wstl = Wstl("ODIS - Service Node Information")
        wstl = wstl.with_get_action("self", "odis-node")
        wstl = wstl.with_get_action("home", "odis-home")
        wstl = wstl.with_get_action("odis:connections", "odis-node-connections")
        wstl = wstl.with_get_action("odis:memberships", "odis-node-memberships")
        wstl = wstl.with_get_action("odis:connect", "odis-node-connect")
        wstl = wstl.add_data_item(
            {
                "id": settings.ODIS_SERVICE_ID,
                "service": settings.ODIS_SERVICE_NAME,
                "version": Odis.version,
                "organisation": "Sample Organisation",
                "contactPoint": "Michal Poreba",
            }
        )

        return Response(wstl.to_data())


class NodeConnections(APIView):
    def get(self, request):
        wstl = Wstl("ODIS - Node's Connections")
        wstl = wstl.with_get_action("self", "odis-node-connections")
        wstl = wstl.with_get_action("home", "odis-home")

        for c in Connection.objects.all():
            wstl.add_data_item(ConnectionSerializer(c).data)

        return Response(wstl.to_data())


class NodeConnection(APIView):
    def get(self, request, id):
        try:
            connection = Connection.objects.get(uuid=id)
            return Response(ConnectionSerializer(connection).data)
        except Connection.DoesNotExist:
            raise Http404

    def approve(connection: Connection):
        connection.approve()

    def reject(connection: Connection):
        connection.reject()

    def disconnect(connection: Connection):
        connection.disconnect()

    def reconnect(connection: Connection):
        connection.reconnect()

    def post(self, request, id, action):
        try:
            connection = Connection.objects.get(uuid=id)
        except Connection.DoesNotExist:
            raise Http404

        implementation = {
            'approve': NodeConnection.approve,
            'reject': NodeConnection.reject,
            'disconnect': NodeConnection.disconnect,
            'reconnect': NodeConnection.reconnect,
        }.get(action.lower(), None)

        if not implementation: 
            raise HttpResponseBadRequest() 

        try: 
            implementation(connection)
            connection.save()
        except RuntimeError:
            raise HttpResponseBadTransition()
    
        return Response(ConnectionSerializer(connection).data)


class NodeMemberships(APIView):
    def get(self, request):
        wstl = Wstl("ODIS - Node's Memberships")
        wstl = wstl.with_get_action("self", "odis-node-memberships")
        wstl = wstl.with_get_action("home", "odis-home")

        for m in Membership.objects.all():
            wstl.add_data_item(MembershipSerializer(m).data)

        return Response(wstl.to_data())


class NodeConnection(APIView):
    def get(self, request, id):
        try:
            connection = Membership.objects.get(uuid=id)
            return Response(MembershipSerializer(connection).data)
        except Membership.DoesNotExist:
            raise Http404


class NodeConnect(APIView):
    def post(self, request, format=None): 
        url = request.data['url']
        type = request.data['type']
        try:
            connection = Connection.objects.get(url=url)
        except Connection.DoesNotExist: 
            connection = Connection(
                url=request.data['url'],
            )

        connection.type = type
        connection.save()

        wstl = Wstl("ODIS - Connection Request")
        wstl = wstl.with_get_action("home", "odis-home")
        wstl = wstl.with_get_action("odis:connections", "odis-node-connections")
        wstl = wstl.add_data_item(ConnectionSerializer(connection).data)
        return Response(wstl.to_data())


class ServiceDescription(APIView):
    def get(self, request):
        # TODO: load from the web, or based on settings
        with open("../../odis.json", "r") as f:
            alps_data = json.load(f)

        wstl = Wstl("Data Exchange Network - ALPS")
        wstl = wstl.with_get_action("self", "odis-alps")
        wstl = wstl.with_get_action("home", "odis-home")
        wstl = wstl.add_data_item(alps_data)
        return Response(wstl.to_data())


class ThisOrganisation(APIView):
    def get(self, request): 
        service = Organisation.objects.get(uuid=settings.ODIS_ORG_ID)
        return Response(OrganisationSerlializer(service).data)


class ThisService(APIView):
    def get(self, request): 
        service = Service.objects.get(uuid=settings.ODIS_SERVICE_ID)
        return Response(ServiceSerializer(service).data)

