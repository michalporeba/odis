from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from odis.odiscomponents import OdisComponent
import requests 
from diogi.functions import always_a_list

class SearchHelp(APIView):
    def get(self, request):
        return Response('to learn how to search check out https://github.com/michalporeba/odis/')


class Search(APIView):
    def get(self, request):
        connections = OdisComponent.get_usable_connections_for('demo:simple-search')
        if connections is None:
            return Response('there are no connections')
        
        headers = {
            'Accept': f'application/json'
        }

        results = []
        for (id, type, url) in connections: 
            response = requests.get(url, headers=headers, params = request.query_params)
            results = results+always_a_list(response.json())
        return Response(results)