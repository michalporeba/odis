import uuid
from django.db import models

MAX_URL_LENGTH = 256

class OdisModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cts = models.DateTimeField(auto_now_add=True)
    uts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True