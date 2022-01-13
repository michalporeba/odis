import requests
from requests.sessions import HTTPAdapter 
from .poly import Poly 
from .wstl import Wstl 
from .hal import Hal 

class RestClient: 
    def __init__(self):
        self.formatter = None
        self.poly = Poly()

    def get(self, url: str) -> Poly:
        headers = {
            'Accept': f'{Wstl.MIME_TYPE}, {Hal.MIME_TYPE}, application/json'
        }

        response = requests.get(url, headers=headers) 
        if 'Accept' in response.headers:
            if Wstl.MIME_TYPE in response.headers['Accept']:
                self.formatter = Wstl
                self.poly = Wstl.parse(response.json())
            if 'application/json' in response.headers['Accept']:
                self.poly = Poly()
                self.poly.add_data_item(response.json())
        
        return self.poly
    
    def do(self, action: str) -> Poly: 
        headers = {
            'Accept': self.formatter.MIME_TYPE
        }

        url = [a for a in self.poly.actions if a.name == action][0].url
        response = requests.get(url, headers=headers)
        self.poly = self.formatter.parse(response.json())

        return self.poly 