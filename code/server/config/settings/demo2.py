from .local import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db2.sqlite3",
    }
}

ODIS_SERVICE_ID = 'e4023ff6-f955-4aae-9011-6e35c4a0f8a4'
ODIS_SERVICE_NAME = 'ODIS Demo 2'
ODIS_SERVICE_ROOT_URL = 'http://127.0.0.1:8082/'