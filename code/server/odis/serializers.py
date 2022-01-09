from rest_framework import serializers
from .models import Connection

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ['uuid', 'cts', 'uts', 'url', 'state']
