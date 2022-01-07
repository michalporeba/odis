from .wstl import WstlContextProvider
from django.urls import get_resolver
from django_kinder_settings import settings

settings.register_if_missing('WSTL_ROOT_URL', '')

class DjangoWstlContextProvider(WstlContextProvider):
    def get_action_url(self, name: str) ->str:
        urls = get_resolver().reverse_dict
        if name in urls.keys():
            (data, _, _, _) = urls[name]
            if len(data)>0:
                (url, _) = data[0]
                return settings.WSTL_ROOT_URL+url
        return None            

        

