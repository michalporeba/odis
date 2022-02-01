from django.urls import path
from .views import *


urlpatterns = [
    path("", Hello.as_view(), name="odis-home"),
    path("node/", Node.as_view(), name="odis-node"),
    path("node/connect/", NodeConnect.as_view(), name="odis-node-connect"),
    path("node/connections/<uuid:id>/<str:action>/", NodeConnection.as_view(), name="odis-node-connection-action"),
    path("node/connections/<uuid:id>/", NodeConnection.as_view(), name="odis-node-connection"),
    path("node/connections/", NodeConnections.as_view(), name="odis-node-connections"),
    path("node/memberships/", NodeMemberships.as_view(), name="odis-node-memberships"),
    path("node/owner/", ThisOrganisation.as_view(), name="odis-node-owner"),
    path("alps/", ServiceDescription.as_view(), name="odis-alps"),
    path("client/", Client.as_view(), name="test-client"),
    path("service/", ThisService.as_view(), name="odis-service")
    
]
