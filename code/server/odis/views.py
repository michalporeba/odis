from typing import Dict
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .wstl import Wstl, WstlClient
from .wstl_django import DjangoWstlContext
from .models import Connection
from django_kinder_settings import settings
from .apps import Odis 
import json

class Hello(APIView):
  def get(self, request): 
    wstl = Wstl('ODIS - Hello')
    wstl = wstl.with_get_action('self', 'odis-home')
    wstl = wstl.with_get_action('home', 'odis-home')
    wstl = wstl.with_get_action('node', 'odis-node')
    wstl = wstl.with_get_action('alps', 'odis-alps')

    return Response(wstl.to_data())

class Client(APIView):
  def get(self, request):
    client = WstlClient('http://127.0.0.1:8001/odis/')
    return Response(client.hello().to_data())

class Connections(APIView): 
  def get(self, request):
    wstl = Wstl("Data Exchange Network - Connections")
    wstl = wstl.with_get_action('self', 'odis-connections')
    wstl = wstl.with_get_action('home', 'odis-home')
    
    for c in Connection.objects.all():
      wstl.add_data_item({
        "uuid": c.uuid,
        "cts": c.cts, 
        "uts": c.uts, 
        "url": c.url,
        "state": c.state 
      })

    return Response(wstl.to_data())


class Service(APIView):
  def get(self, request):
    wstl = Wstl("ODIS - Service Node Information")
    wstl = wstl.with_get_action('self', 'odis-node')
    wstl = wstl.with_get_action('home', 'odis-home')
    wstl = wstl.add_data_item({
      "id": settings.ODIS_SERVICE_ID,
      "service": settings.ODIS_SERVICE_NAME,
      "version": Odis.version,
      "organisation": 'Sample Organisation',
      "contactPoint": 'Michal Poreba'
    })

    return Response(wstl.to_data())

class ServiceDescription(APIView):
  def get(self, request):
    # TODO: load from the web, or based on settings
    with open('../../odis.json', 'r') as f:
      alps_data = json.load(f)

    wstl = Wstl("Data Exchange Network - ALPS")
    wstl = wstl.with_get_action('self', 'odis-alps')
    wstl = wstl.with_get_action('home', 'odis-home')
    wstl = wstl.add_data_item(alps_data)
    return Response(wstl.to_data())

class Target(APIView):
  def get(self, request):
    return Response({
      "wstl": {
        "actions": [],
        "data": [],
      }
    })

# Create your views here.
class WstlSample(APIView):
    def get(self, request, format='not-provider'):
        return Response({
  "wstl": {
    "actions": [
      {
        "name": "homeLink",
        "description" : "View the home page",
        "type": "safe",
        "action": "read",
        "kind": "",
        "target": "list menu",
        "prompt": "Home",
      },
      {
        "name": "searchForm",
        "description" : "Search for content",
        "type": "safe",
        "action": "read",
        "kind": "search",
        "target": "list form",
        "prompt": "Search",
        "inputs": [
          {
            "name": "text",
            "prompt": "Search Text",
            "value": "Danny",
            "required" : True
          },
          {
            "name": "external",
            "prompt": "External Search?",
            "value": "",
            "required": True,
            "suggest": [{"value":"true"},{"value":"false"}]
          }
        ]
      }
    ],
    "data": [
      {
        "id": "1a14qx7qc81",
        "title": "Danny Boy"
      },
      {
        "id": "1q2w3e43r",
        "title": "Danny Tremane"
      },
      {
        "id": "azsxdcfvgb",
        "title": "Danny Two-Shoes"
      },
    ]
  }
})