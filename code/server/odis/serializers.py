from rest_framework import serializers
from .models import Connection, Organisation, Service, Membership


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ["uuid", "cts", "uts", "url", "state"]


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership 
        fields = ['uuid', 'cts', 'uts', 'url', 'current_state', 'expected_state']


class OrganisationSerlializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Organisation
        fields = ['uuid', 'name']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ["uuid", "name"]
