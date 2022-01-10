from django.apps import AppConfig


class DenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'odis'

# TODO: perhaps there is a better place for this
class Odis:
    version = "0.0.1"

    