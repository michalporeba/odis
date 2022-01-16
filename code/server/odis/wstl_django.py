from .wstl import WstlContext
from django.urls import get_resolver
from django_kinder_settings import settings


class DjangoWstlContext(WstlContext):
    def get_action_url(name: str) -> str:
        urls = get_resolver().reverse_dict
        if name in urls.keys():
            (data, _, _, _) = urls[name]
            if len(data) > 0:
                (url, _) = data[0]
                return settings.ODIS_SERVICE_ROOT_URL + url
        return None
