from django.apps import AppConfig
from django_kinder_settings import settings


class DenConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "odis"


# TODO: perhaps there is a better place for this
class Odis:
    version = "0.0.1"


settings.register_if_missing(
    name="ODIS_SERVICE_ROOT_URL",
    default="",
    explanation="""
The ODIS_SERVICE_ROOT_URL is used to create action URLs.
It should include protocol, host and if necessary port and path ending with /.
For example: https://myserver.com:8000/abc/
""",
)


settings.register_if_missing(
    name="ODIS_ALPS_URL",
    default="https://raw.githubusercontent.com/michalporeba/odis/main/odis.json",
    explanation="""
The ODIS_ALPS_URL should point at a network location with the current ALPS profile of the service
""",
)
