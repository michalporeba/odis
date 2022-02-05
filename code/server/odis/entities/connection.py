from rest_framework import serializers
from django.db import models
from . import OdisModel, MAX_URL_LENGTH, guard_state_transition

class Connection(OdisModel):
    class States(models.TextChoices):
        ACTIVE = ('A', 'Active')
        DENIED = ('D', 'Denied')
        FAILED = ('F', 'Failed')
        REQUESTED = ('R', 'Requested')
        SUSPENDED = ('S', 'Suspended')
        UNAVAILABLE = ('U', 'Unavailable')
        DISCONNECTED = ('X', 'Disconnected')

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
        self.state = Connection.States.ACTIVE
        
    def reject(self):
        self.state = Connection.States.DENIED
        
    def disconnect(self):
        self.state = Connection.States.DISCONNECTED
        
    def mark_unavailable(self):
        self.state = Connection.States.UNAVAILABLE
        
    def reconnect(self):
        self.state = Connection.States.ACTIVE
            
    def suspend(self):
        self.state = Connection.States.SUSPENDED
        
    def do(self, action: str, *args, **kwargs) -> None: 
        transitions = {
            'approve': [[
                Connection.States.REQUESTED,
                Connection.States.DENIED,
                self.approve
            ]],
            'reject': [[
                Connection.States.REQUESTED,
                self.reject
            ]],
            'disconnect': [
                self.disconnect
            ],
            'reconnect': self.reconnect,
            'mark_unavailable': self.mark_unavailable,
            'suspend': [[
                Connection.States.ACTIVE, self.suspend
            ]]
        }
        guard_state_transition(transitions, action, self.state, *args, **kwargs)


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ['uuid', 'cts', 'uts', 'url', 'state', 'type']
