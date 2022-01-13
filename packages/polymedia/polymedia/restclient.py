import requests
from requests.models import Response
from .poly import Poly 
from .wstl import Wstl 
from .hal import Hal 

class RestClient: 
    def __init__(self):
        self.formatter = None
        self.format = 'json'
        self.poly = Poly()
        self._accepted_types = ''

    def get(self, url: str) -> Poly:
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
        
        return self.poly
    
    def do(self, action: str) -> Poly: 
        headers = {
            'Accept': self._accepted_types
        }

        url = [a for a in self.poly.actions if a.name == action][0].url
        response = requests.get(url, headers=headers)
        
        self.poly = self.formatter.parse(response.json())

        return self.poly 

    def actions(self) -> list:
        return [a.name for a in self.poly.actions]

    def can_do(self, action: str) -> bool: 
        return 0 < len([a for a in self.poly.actions if a.name == action])