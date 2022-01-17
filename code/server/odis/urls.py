from django.urls import path
from .views import *


urlpatterns = [
    path("", Hello.as_view(), name="odis-home"),
    path("node/", Node.as_view(), name="odis-node"),
    path("node/connect", NodeConnect.as_view(), name="odis-node-connect"),
    path("node/owner/", ThisOrganisation.as_view(), name="odis-node-owner"),
    path("alps/", ServiceDescription.as_view(), name="odis-alps"),
    path("connections/", Connections.as_view(), name="odis-connections"),
    path("client/", Client.as_view(), name="test-client"),
    path("service/", ThisService.as_view(), name="odis-service")
    
]
