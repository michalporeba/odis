from .poly import *

class Hal: 
    MIME_TYPE = 'application/vnd.hal+json'
    def format(poly: Poly) -> dict: 
        return {}

    def parse(hal: dict) -> Poly: 
        return Poly().set_title('HAL is currently not supported')