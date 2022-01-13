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


def test_data():
    poly = Poly()
    poly.add_data_item(1)
    data = poly.to(Wstl)['wstl']['data'][0]
    assert 1 == data


def test_create_empty_poly_from_empty_wstl():
    poly = Wstl.parse({ 'wstl': {}})
    assert None == poly.title


def test_create_poly_from_wstl_with_singles():
    poly = Wstl.parse({ 'wstl': {
        'title': 'sample title',
        'actions': { 'name': 'test.action', 'url': 'test://url.com'},
        'data': { 'a': 1, 'b': 3 }
    }})
    assert 'sample title' == poly.title 
    action = poly.actions[0]
    assert 'test.action' == action.name
    assert 'test://url.com' == action.url
    data = poly.data[0]
    assert 1 == data['a']
    assert 3 == data['b']


def test_create_poly_from_wstl_with_multiples():
    poly = Wstl.parse({ 'wstl': {
        'actions': [
            { 'name': 'dosomething', 'url': 'a.url.com'},
            { 'name': 'second.action', 'url': 'test://url.co.uk'},
        ],
        'data': [
            { 'a': 'a', 'b': 'b' },
            { 'a': 11, 'b': 33 }
        ]
    }})
    action = poly.actions[1]
    assert 'second.action' == action.name
    assert 'test://url.co.uk' == action.url
    data = poly.data[1]
    assert 11 == data['a']
    assert 33 == data['b']