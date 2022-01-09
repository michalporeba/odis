from django.urls import path

from .views import *

urlpatterns = [
    path('', Hello.as_view(), name='odis-home'),
    path('service/', Service.as_view(), name='odis-service'),
    path('target/', Target.as_view(), name='odis-target'),
    path('sample/', WstlSample.as_view(), name='odis-sample'),
    path('connections/', Connections.as_view(), name='odis-connections')
]