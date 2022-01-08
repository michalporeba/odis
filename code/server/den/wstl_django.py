from .wstl import WstlContext
from django.urls import get_resolver
from django_kinder_settings import settings

settings.register_if_missing(
    name='WSTL_ROOT_URL',
    default='',
    explanation='''
The WSTL_ROOT_URL is used to create action URLs.
It should include protocol, host and if necessary port and path ending with /.
For example: https://myserver.com:8000/abc/
''')

class DjangoWstlContext(WstlContext):
    def get_action_url(name: str) ->str:
        urls = get_resolver().reverse_dict
        if name in urls.keys():
            (data, _, _, _) = urls[name]
            if len(data)>0:
                (url, _) = data[0]
                return settings.WSTL_ROOT_URL+url
        return None            