from django.db import models
from rest_framework import serializers
from . import OdisModel, MAX_URL_LENGTH


# https://schema.org/Organization
class Organisation(OdisModel):
    name = models.CharField(max_length=128, unique=True, blank=False, null=False)
    url = models.CharField(
        max_length=MAX_URL_LENGTH, unique=True, blank=False, null=False
    )
    logo = models.CharField(max_length=MAX_URL_LENGTH, blank=True, null=True)


class OrganisationSerlializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Organisation
        fields = ['uuid', 'name']