from django.urls import path

from .views import *
urlpatterns = [
    path('', Hello.as_view()),
    path('target/', Target.as_view()),
    path('sample/', WstlSample.as_view())
]