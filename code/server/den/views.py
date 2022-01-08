from typing import Dict
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .wstl import Wstl
from .wstl_django import DjangoWstlContext
from .models import Connection

class Hello(APIView):
  def get(self, request): 
    wstl = Wstl('Data Exchange Network - Hello')
    wstl = wstl.with_get_action('self', 'den-home')
    wstl = wstl.with_get_action('home', 'den-home')
    wstl = wstl.with_get_action('info', 'den-info')

    return Response(wstl.to_data())

class Info(APIView):
  def get(self, request):
    wstl = Wstl("Data Exchange Network - Node's Status")
    wstl = wstl.with_get_action('self', 'den-info')
    wstl = wstl.with_get_action('home', 'den-home')
    wstl = wstl.add_data_item({
      "version": '0.0.1',
      "organisation": 'Sample Organisation',
      "contactPoint": 'Michal Poreba'
    })

    return Response(wstl.to_data())

class Connections(APIView): 
  def get(self, request):
    wstl = Wstl("Data Exchange Network - Connections")
    wstl = wstl.with_get_action('self', 'den-connections')
    wstl = wstl.with_get_action('home', 'den-home')
    
    for c in Connection.objects.all():
      wstl.add_data_item({
        "uuid": c.uuid,
        "cts": c.cts, 
        "uts": c.uts, 
        "url": c.url,
        "state": c.state 
      })

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