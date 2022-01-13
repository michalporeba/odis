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

    def get(self, url: str) -> Poly:
        headers = {
            'Accept': f'{Wstl.MIME_TYPE}, {Hal.MIME_TYPE}, application/json'
        }

        def set_wstl(response: Response):
            self.formatter = Wstl
            self.format = 'wstl'
            self.poly = Wstl.parse(response.json())

        response = requests.get(url, headers=headers) 
        if 'Accept' in response.headers:
            if Wstl.MIME_TYPE in response.headers['Accept']:
                set_wstl(response)
            if 'application/json' in response.headers['Accept']:
                data = response.json()
                if 'wstl' in data.keys(): 
                    set_wstl(response)
                else: 
                    self.poly = Poly()
                    self.poly.add_data_item(data)
        else: 
            data = response.json()
            if 'wstl' in data.keys(): 
                set_wstl(response)


        return self.poly
    
    def do(self, action: str) -> Poly: 
        headers = {
            'Accept': self.formatter.MIME_TYPE
        }

        url = [a for a in self.poly.actions if a.name == action][0].url
        response = requests.get(url, headers=headers)
        self.poly = self.formatter.parse(response.json())

        return self.poly 

    def actions(self) -> list:
        return [a.name for a in self.poly.actions]

    def can_do(self, action: str) -> bool: 
        return 0 < len([a for a in self.poly.actions if a.name == action])