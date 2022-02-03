from rest_framework import serializers
from django.db import models
from .base import OdisModel, MAX_URL_LENGTH

class Connection(OdisModel):
    class States(models.TextChoices):
        ACTIVE = ("A", "Active")
        DENIED = ("D", "Denied")
        FAILED = ("F", "Failed")
        REQUESTED = ("R", "Requested")
        SUSPENDED = ("S", "Suspended")
        UNAVAILABLE = ("U", "Unavailable")
        DISCONNECTED = ("X", "Disconnected")

        @classmethod
        def get_valid_transitions() -> list:
            return [
                (Connection.States.REQUESTED, Connection.States.ACTIVE),
                (Connection.States.REQUESTED, Connection.States.DENIED),
                (Connection.States.DENIED, Connection.States.ACTIVE),
                (Connection.States.ACTIVE, Connection.States.DISCONNECTED),
                (Connection.States.ACTIVE, Connection.States.SUSPENDED),
                (Connection.States.ACTIVE, Connection.States.UNAVAILABLE)
            ]

    url = models.CharField(
        max_length=MAX_URL_LENGTH, unique=True, editable=False, blank=False, null=False
    )
    state = models.CharField(
        max_length=1,
        choices=States.choices,
        default=States.REQUESTED,
        blank=False,
        null=False,
    )
    type = models.CharField(
        max_length = 16,
        blank = False, 
        null = False
    )

    def approve(self):
        if self.state == Connection.States.ACTIVE:
            return 
        if self.state != Connection.States.REQUESTED:
            raise RuntimeError
        self.state = Connection.States.ACTIVE

    def reject(self):
        if self.state == Connection.States.DENIED:
            return 
        if self.state != Connection.States.REQUESTED:
            raise RuntimeError
        self.state = Connection.States.DENIED

    def disconnect(self):
        if self.state == Connection.States.DISCONNECTED:
            return 
        if self.state in [
            Connection.States.ACTIVE, 
            Connection.States.FAILED,
            Connection.States.SUSPENDED,
            Connection.States.UNAVAILABLE
            ]:
            self.state = Connection.States.DISCONNECTED
        else: 
            raise RuntimeError

    def reconnect(self):
        if self.state == Connection.States.ACTIVE:
            return 
        if self.state in [Connection.States.DISCONNECTED]:
            self.state = Connection.States.ACTIVE
        else: 
            raise RuntimeError


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ['uuid', 'cts', 'uts', 'url', 'state', 'type']
