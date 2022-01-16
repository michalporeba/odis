import requests
from alps import Alps, Unsafe
from .poly import Poly 
from .wstl import Wstl 
from .hal import Hal 
from diogi.functions import first_or_default


def get_alps():
    pass


class RestClient: 
    def __init__(self):
        self.formatter = None
        self.format = 'json'
        self.poly = Poly()
        self._accepted_types = ''
        self._alps = None 

    def connect(self, url: str) -> Poly:
        headers = {
            'Accept': f'{Wstl.MIME_TYPE}, {Hal.MIME_TYPE}, application/json'
        }
        
        response = requests.get(url, headers=headers) 
        self._accepted_types = response.headers['Content-Type']
        data = response.json()

        if 'wstl' in data.keys(): 
            self.format = 'wstl'
            self.formatter = Wstl
            self.poly = Wstl.parse(response.json())
        else: 
            self.poly = Poly()
            self.poly.add_data_item(data)
        
        self._detect_and_set_alps()

        return self.poly

    def get(self, action: str, resolver: callable = None) -> dict:
        params = self._resolve_params(action, resolver)
        url = [a for a in self.poly.actions if a.name == action][0].url
        response = None

        if self.alps is not None:
            descriptor = self.alps.get_descriptor(action)
            if descriptor is not None:
                if isinstance(descriptor, Unsafe):
                    headers = {'Accept': 'application/json'}
                    response = requests.post(url, headers=headers, json=params)
        if response is None:
            headers = {'Accept': self._accepted_types}
            response = requests.get(url, headers=headers, params=params)

        return self.formatter.parse(response.json())

    def do(self, action: str, resolver: callable = None) -> Poly:
        self.poly = self.get(action, resolver)
        self._detect_and_set_alps()
        return self.poly 

    @property 
    def alps(self) -> Alps | None:
        return self._alps

    @property
    def actions(self) -> list:
        return [a.name for a in self.poly.actions]

    def can_do(self, action: str) -> bool: 
        return 0 < len([a for a in self.poly.actions if a.name == action])

    def _detect_and_set_alps(self):
        if self.can_do('alps'):
            poly = self.get('alps')
            alps_data = first_or_default(poly.data,{})
            self._alps = Alps.parse(alps_data, Alps.default_resolver(alps_data))

    def _resolve_params(self, action: str, resolver: callable) -> dict:
        if resolver is None or self.alps is None:
            return {}
        
        descriptor = self.alps.get_descriptor(action)
        
        params = {}
        for d in descriptor.descriptors:
            params[d.id] = resolver(d)

        return params
