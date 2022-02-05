from rest_framework import serializers
from django.db import models
from . import OdisModel, MAX_URL_LENGTH, guard_state_transition


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


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership 
        fields = ['uuid', 'cts', 'uts', 'url', 'current_state', 'expected_state']
