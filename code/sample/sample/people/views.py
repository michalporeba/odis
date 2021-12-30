from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics

# Create your views here.

from .serializers import * 


class CarOwnershipView(generics.ListAPIView):
    serializer_class = CarOwnershipSerializer

    def get_queryset(self):
        queryset = CarOwnership.objects.all()
        query = self.request.query_params.get('q', None)
        if query is not None:
            return queryset.filter(owner__contains=query)
        return queryset

class DrivingLicenseView(generics.ListAPIView):
    serializer_class = DrivingLicenseSerializer

    def get_queryset(self):
        queryset = DrivingLicense.objects.all()
        query = self.request.query_params.get('q', None)
        if query is not None:
            return queryset.filter(name__contains=query)
        return queryset


class EmploymentView(generics.ListAPIView):
    serializer_class = EmploymentSerializer

    def get_queryset(self):
        queryset = Employment.objects.all()
        query = self.request.query_params.get('q', None)
        if query is not None:
            return queryset.filter(name__contains=query)
        return queryset