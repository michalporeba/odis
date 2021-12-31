from django.urls import path

from .views import *
urlpatterns = [
    path('cars/', CarOwnershipView.as_view(), name='cars'),
    path('employment/', EmploymentView.as_view(), name='employment'),
    path('licenses/', DrivingLicenseView.as_view(), name='licenses')
]