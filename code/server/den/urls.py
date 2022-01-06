from django.urls import path

from .views import *
urlpatterns = [
    path('', Hello.as_view(), name='den-hello'),
    path('target/', Target.as_view(), name='den-target'),
    path('sample/', WstlSample.as_view(), name='den-sample')
]