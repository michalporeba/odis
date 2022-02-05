from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class SearchHelp(APIView):
    def get(self, request):
        return Response('to learn how to search check out https://github.com/michalporeba/odis/')


class Search(APIView):
    def get(self, request):
        return Response('')