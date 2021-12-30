from django.contrib import admin

from .models import CarOwnership, Employment, DrivingLicense 

# Register your models here.

admin.site.register(CarOwnership)
admin.site.register(DrivingLicense)
admin.site.register(Employment)