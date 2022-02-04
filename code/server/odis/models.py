import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from .entities import OdisModel, MAX_URL_LENGTH
from .entities.connection import Connection


class Membership(OdisModel):
    class MembershipStates(models.TextChoices):
        ACTIVE = ("A", "Active")
        DENIED = ("D", "Denied")
        REQUESTED = ("R", "Requested")
        SUSPENDED = ("S", "Suspended")
        DISCONNECTED = ("X", "Disconnected")    

    url = models.CharField(
        max_length=MAX_URL_LENGTH, unique=True, editable=False, blank=False, null=False
    )
    current_state = models.CharField(
        max_length=1,
        choices=MembershipStates.choices,
        default=MembershipStates.REQUESTED,
        blank=False,
        null=False,
    )
    expected_state = models.CharField(
        max_length=1,
        choices=MembershipStates.choices,
        default=MembershipStates.ACTIVE,
        blank=False,
        null=False,
    )


# https://schema.org/Organization
class Organisation(OdisModel):
    name = models.CharField(max_length=128, unique=True, blank=False, null=False)
    url = models.CharField(
        max_length=MAX_URL_LENGTH, unique=True, blank=False, null=False
    )
    logo = models.CharField(max_length=MAX_URL_LENGTH, blank=True, null=True)


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
