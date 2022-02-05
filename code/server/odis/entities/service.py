from django.db import models
from django.db.models.deletion import CASCADE
from rest_framework import serializers
from . import OdisModel, MAX_URL_LENGTH
from .organisation import Organisation


# https://schema.org/Service
class Service(OdisModel):
    name = models.CharField(max_length=128, unique=True, blank=False, null=False)
    url = models.CharField(
        max_length=MAX_URL_LENGTH, unique=True, blank=False, null=False
    )
    audience_type = models.CharField(max_length=32, blank=True, null=True)
    audience_administrative_area_name = models.CharField(
        max_length=64, blank=True, null=True
    )
    category = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField()
    logo = models.CharField(max_length=MAX_URL_LENGTH, blank=True, null=True)
    provider = models.ForeignKey(Organisation, on_delete=CASCADE)


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ["uuid", "name"]