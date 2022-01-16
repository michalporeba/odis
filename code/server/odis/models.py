import uuid
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
MAX_URL_LENGTH = 256


class DisModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cts = models.DateTimeField(auto_now_add=True)
    uts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Connection(DisModel):
    class ConnectionStates(models.TextChoices):
        REQUESTED = ("R", "Requested")
        CONNECTED = ("C", "Connected")
        DENIED = ("D", "Denied")

    url = models.CharField(
        max_length=MAX_URL_LENGTH, unique=True, editable=False, blank=False, null=False
    )
    state = models.CharField(
        max_length=1,
        choices=ConnectionStates.choices,
        default=ConnectionStates.REQUESTED,
        blank=False,
        null=False,
    )


# https://schema.org/Organization
class Organisation(DisModel):
    name = models.CharField(max_length=128, unique=True, blank=False, null=False)
    url = models.CharField(
        max_length=MAX_URL_LENGTH, unique=True, blank=False, null=False
    )
    logo = models.CharField(max_length=MAX_URL_LENGTH, blank=True, null=True)


# https://schema.org/Service
class Service(DisModel):
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
