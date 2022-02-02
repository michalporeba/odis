from rest_framework import serializers
from .models import Organisation, Service, Membership
from .entities.connection import ConnectionSerializer

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
