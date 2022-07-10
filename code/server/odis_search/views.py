from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from odis.odiscomponents import OdisComponent
from diogi.functions import always_a_list
from .plugins.odis import search_in_odis_node
from .plugins.simple_demo import search_in_simple_demo

class SearchHelp(APIView):
    def get(self, request):
        return Response('to learn how to search check out https://github.com/michalporeba/odis/')


class Search(APIView):
    def get(self, request):
        connections = OdisComponent.get_usable_connections_for('demo')
        if connections is None:
            return Response(None)
        
        results = []
        for (id, type, url) in connections: 
            print(f'{type} {url}')
            implementation = {
                'odis': search_in_odis_node,
                'demo:simple-search': search_in_simple_demo
            }.get(type.lower(), None)

            if implementation is None: 
                # TODO: log unsupported type
                continue 

            query = request.query_params.get('q', '')
            # TODO: this should be done in parallel 
            results = results+always_a_list(implementation(url, query))

        return Response(results)