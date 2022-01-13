import requests 
from .poly import Poly 
from .wstl import Wstl 

class RestClient: 
    def __init__(self):
        pass

    def hello(self, url: str) -> Poly:
        response = requests.get(url) 
        return Wstl.parse(response.json())