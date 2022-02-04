from pkgutil import ImpLoader
from sys import implementation
from rest_framework import serializers
from django.db import models
from . import OdisModel, MAX_URL_LENGTH, TextState

class Connection(OdisModel):
    class States(TextState, models.enums.Choices):
        ACTIVE = ('A', 'Active', ['R', 'D', 'S', 'U', 'X'])
        DENIED = ('D', 'Denied', ['R'])
        FAILED = ('F', 'Failed', ['R'])
        REQUESTED = ('R', 'Requested')
        SUSPENDED = ('S', 'Suspended', ['A'])
        UNAVAILABLE = ('U', 'Unavailable', ['A'])
        DISCONNECTED = ('X', 'Disconnected', ['A'])

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
        print('testing')
        next = Connection.States.ACTIVE
        if self.state == next:
            return 
        if Connection.States.is_valid_transition(self.state, next):
            raise RuntimeError
        self.state = next

    def reject(self):
        next = Connection.States.DENIED
        if self.state == next:
            return 
        if Connection.States.is_valid_transition(self.state, next):
            raise RuntimeError
        self.state = next

    def disconnect(self):
        next = Connection.States.DISCONNECTED
        if self.state == next:
            return 
        if not Connection.States.is_valid_transition(self.state, next):
            raise RuntimeError
        self.state = next

    def mark_unavailable(self):
        next = Connection.States.UNAVAILABLE
        if self.state == next:
            return
        if not Connection.States.is_valid_transition(self.state, next):
            raise RuntimeError
        self.state = Connection.States.UNAVAILABLE

    def reconnect(self):
        next = Connection.States.ACTIVE
        if self.state == next:
            return 
        if not Connection.States.is_valid_transition(self.state, next):
            raise RuntimeError
        self.state = Connection.States.ACTIVE
            
    def suspend(self):
        next = Connection.States.SUSPENDED
        if self.state == next:
            return 
        Connection.States.check_transition(self.state, next)
        self.state = Connection.States.SUSPENDED

    def do(self, action: str) -> None: 
        implementation = {
            'approve': self.approve,
            'reject': self.reject,
            'disconnect': self.disconnect,
            'reconnect': self.reconnect,
            'mark_unavailable': self.mark_unavailable,
            'suspend': self.suspend 
        }.get(action.lower(), None)

        if (implementation is None):
            raise RuntimeError

        implementation() 


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ['uuid', 'cts', 'uts', 'url', 'state', 'type']
