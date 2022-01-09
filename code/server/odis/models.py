import uuid 
from django.db import models

# Create your models here.

class DisModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cts = models.DateTimeField(auto_now_add=True)
    uts = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True 

class Connection(DisModel):
    class ConnectionStates(models.TextChoices):
        REQUESTED = ('R','Requested')
        CONNECTED = ('C','Connected')
        DENIED = ('D','Denied')

    url = models.CharField(
        max_length=256,
        unique=True,
        editable=False,
        blank=False,
        null=False
    )
    state = models.CharField(
        max_length=1,
        choices=ConnectionStates.choices,
        default=ConnectionStates.REQUESTED,
        blank=False,
        null=False
    )
