from django.urls import path

from .views import *

urlpatterns = [
    path('', Hello.as_view(), name='odis-home'),
    path('node/', Service.as_view(), name='odis-node'),
    path('alps/', ServiceDescription.as_view(), name='odis-alps'),
    path('target/', Target.as_view(), name='odis-target'),
    path('sample/', WstlSample.as_view(), name='odis-sample'),
    path('connections/', Connections.as_view(), name='odis-connections'),
    path('client/', Client.as_view(), name='test-client')
]