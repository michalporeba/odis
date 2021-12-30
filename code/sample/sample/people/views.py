from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions 
from .serializers import * 


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classess = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CarOwnershipViewSet(viewsets.ModelViewSet):
    queryset = CarOwnership.objects.all()
    serializer_class = CarOwnershipSerializer


class DrivingLicenseViewSet(viewsets.ModelViewSet):
    queryset = DrivingLicense.objects.all()
    serializer_class = DrivingLicenseSerializer


class EmploymentViewSet(viewsets.ModelViewSet):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer


def carownership_list(request):
    if request.method == 'GET':
        data = CarOwnership.objects.all()
        serializer = CarOwnershipSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


def drivinglicenses_list(request):
    if request.method == 'GET':
        data = DrivingLicense.objects.all()
        serializer = DrivingLicenseSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


def employment_list(request): 
    if request.method == 'GET':
        data = Employment.objects.all()
        serializer = EmploymentSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)