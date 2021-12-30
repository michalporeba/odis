from django.urls import path

from .views import *
urlpatterns = [
    path('cars/', CarOwnershipView.as_view()),
    path('employment/', EmploymentView.as_view()),
    path('licenses/', DrivingLicenseView.as_view())
]