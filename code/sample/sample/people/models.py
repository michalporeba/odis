from abc import abstractclassmethod
from django.db import models

# Create your models here.

class AddressMixin(models.Model):
    address = models.CharField("Address", max_length=128, blank=False, null=False)
    city = models.CharField("City", max_length=64, blank=False, null=False)
    postcode = models.CharField("PostCode", max_length=32, blank=False, null=False)

    class Meta:
        abstract = True 


class DrivingLicense(AddressMixin):
    date = models.DateField("Date", blank=False, null=False)
    name = models.CharField("Name", max_length=128, blank=False, null=False)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        app_label = 'people'

    
class CarOwnership(AddressMixin):
    date = models.DateField("Date", blank=False, null=False)
    owner = models.CharField("Name", max_length=128, blank=False, null=False)
    make = models.CharField("Make", max_length=32, blank=False, null=False)
    model = models.CharField("Model", max_length=32, blank=False, null=False)

    def __str__(self):
        return f"{self.make} {self.model} (@ {self.date})"

    class Meta: 
        app_label = 'people'


class Employment(models.Model):
    date = models.DateField("Date", blank=False, null=False)
    name = models.CharField("Name", max_length=128, blank=False, null=False)
    employer = models.CharField("Employer", max_length=32, blank=False, null=False)
    department = models.CharField("Department", max_length=32, blank=False, null=False)

    def __str__(self):
        return f"{self.name} at {self.employer} in {self.department}"

    class Meta: 
        app_label = 'people'