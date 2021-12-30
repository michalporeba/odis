from django.urls import path

from .views import carownership_list, drivinglicenses_list, employment_list

urlpatterns = [
    path('cars/', carownership_list),
    path('employment/', employment_list),
    path('licenses/', drivinglicenses_list)
]