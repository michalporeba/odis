from poly.poly import *
from poly.wstl import Wstl

class PolyContextForTesting(PolyContext):
    def get_action_url(action: str) -> str: 
        return {
            'sample': 'https://sample.com/',
            'test-home': 'test://home'
        }[action]

def test_returns_wstl():
    data = Poly().to(Wstl)
    assert 'wstl' in data.keys()


def test_contains_title_if_set():
    poly = Poly()
    data = poly.to(Wstl)['wstl']
    assert 'title' not in data.keys()
    poly.set_title('mytitle')
    data = poly.to(Wstl)['wstl']
    assert 'mytitle' == data['title']


def test_home_and_self_actions():
    poly = Poly()
    data = poly.to(Wstl)['wstl']
    assert 'actions' not in data.keys()
    
    poly.add_action(Home('test-home'))
    data = poly.to(Wstl)['wstl']
    assert 1 == len(data['actions'])
    action = data['actions'][0]
    assert 'home' == action['name']
    assert 'safe' == action['type']
    assert 'test://home' == action['url']
    
    poly.add_action(Self('sample'))
    action = poly.to(Wstl)['wstl']['actions'][1]
    assert 'self' == action['name']
    assert 'safe' == action['type']
    assert 'https://sample.com/' == action['url']


def test_get_action():
    poly = Poly()
    poly.add_action(Get('sample'))
    