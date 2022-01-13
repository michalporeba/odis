from .poly import *
from diogi.functions import (
    always_a_list,
    get_if_exists, 
    none_if_empty, 
    set_if_not_none
)

def action(action: Action) -> dict:
        action_type = 'safe'
        return {
            'name': action.name, 
            'type': action_type, 
            'url': action.url
        } 

class Wstl:
    MIME_TYPE = 'application/prs.wstl+json'

    def format(poly: Poly) -> dict:
        data = {}
        set_if_not_none(data, poly.title, 'title')

        actions = list(map(action, poly.actions))
        set_if_not_none(data, none_if_empty(actions), 'actions') 

        set_if_not_none(data, none_if_empty(poly.data), 'data')
        
        return {
            'wstl': data
        }

    def parse(wstl: dict) -> Poly: 
        wstl = wstl['wstl']
        poly = Poly()
        poly.set_title(get_if_exists(wstl, 'title'))

        actions = always_a_list(get_if_exists(wstl, 'actions'))
        for a in actions: 
            poly.actions.append(Action(
                get_if_exists(a, 'name'),
                get_if_exists(a, 'url')
                ))

        data = always_a_list(get_if_exists(wstl, 'data'))
        for d in data: 
            poly.data.append(d)

        return poly