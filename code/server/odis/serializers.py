from rest_framework import serializers
from .models import Connection, Organisation, Service


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ["uuid", "cts", "uts", "url", "state"]


class OrganisationSerlializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Organisation
        fields = ['uuid', 'name']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ["uuid", "name"]
