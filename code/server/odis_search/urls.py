from django.urls import path
from .views import *


urlpatterns = [
    path("search/help/", SearchHelp.as_view(), name="odis-search-help"),
    path("search/", Search.as_view(), name="odis-search")
]
