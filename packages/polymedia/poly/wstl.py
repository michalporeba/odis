from .poly import *
from diogi.functions import *

def action(action: Action) -> dict:
        action_type = 'safe'
        return {
            'name': action.name, 
            'type': action_type, 
            'url': action.url
        } 

class Wstl:
    def format(poly: Poly) -> dict:
        data = {}
        set_if_not_none(data, poly.title, 'title')

        actions = list(map(action, poly.actions))
        set_if_not_none(data, none_if_empty(actions), 'actions') 
        
        return {
            'wstl': data
        }

    