from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import DrivingLicense, CarOwnership, Employment

class DrivingLicenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = DrivingLicense
        fields = ['date', 'name', 'address', 'city', 'postcode']


class CarOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = CarOwnership
        fields = ['date', 'owner', 'make', 'model',  'address', 'city', 'postcode']


class EmploymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employment
        fields = ['date', 'name', 'employer', 'department']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Group, 
        fields = ['url', 'name']