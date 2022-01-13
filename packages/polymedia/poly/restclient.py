import requests 
from .poly import Poly 
from .wstl import Wstl 
from .hal import Hal 

class RestClient: 
    def __init__(self):
        self.formatter = None

    def hello(self, url: str) -> Poly:
        headers = {
            'Accept': f'{Wstl.MIME_TYPE}, {Hal.MIME_TYPE}, application/json'
        }

        response = requests.get(url, headers=headers) 
        if 'Accept' in response.headers:
            if Wstl.MIME_TYPE in response.headers['Accept']:
                self.formatter = Wstl
                return Wstl.parse(response.json())
            if 'application/json' in response.headers['Accept']:
                poly = Poly()
                poly.add_data_item(response.json())
                return poly
        
        return Poly()
        