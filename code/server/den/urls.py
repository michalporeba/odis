from django.urls import path

from .views import *

urlpatterns = [
    path('', Hello.as_view(), name='den-home'),
    path('info/', Info.as_view(), name='den-info'),
    path('target/', Target.as_view(), name='den-target'),
    path('sample/', WstlSample.as_view(), name='den-sample'),
    path('connections/', Connections.as_view(), name='den-connections')
]