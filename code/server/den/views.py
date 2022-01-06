from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 

class Wstl():
  def __init__(self, title: str = ''):
    self._title = title
    self._actions = None
    self._data = None

  def to_data(self):
    data = {}
    if self._actions:
      data['actions'] = self._actions
    if self._data:
      data['data'] = self._data
    if self._title:
      data['title'] = self._title

    return { "wstl": data }

class Hello(APIView):
  def get(self, request): 
    wstl = Wstl('Data Exchange Network - Hello')

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