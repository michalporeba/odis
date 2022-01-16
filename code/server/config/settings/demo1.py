from .local import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db1.sqlite3",
    }
}

ODIS_SERVICE_ID = "6caab3eb-4ef5-4c3d-96e1-6d5ac3b307a2"
ODIS_SERVICE_NAME = "ODIS Demo 1"
ODIS_SERVICE_ROOT_URL = "http://127.0.0.1:8081/"
