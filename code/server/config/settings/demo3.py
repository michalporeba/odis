from .local import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db3.sqlite3",
    }
}

ODIS_SERVICE_ID = '16872c1c-9231-41c3-914e-182c72b40b64'
ODIS_SERVICE_NAME = 'ODIS Demo 3'
ODIS_SERVICE_ROOT_URL = 'http://127.0.0.1:8083/'