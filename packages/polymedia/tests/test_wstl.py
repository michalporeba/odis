from poly.poly import *
from poly.wstl import Wstl

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


def test_home_action():
    poly = Poly()
    data = poly.to(Wstl)['wstl']
    assert 'actions' not in data.keys()
    poly.add_action(Home('test-home'))
    data = poly.to(Wstl)['wstl']
    print(data)
    assert 1 == len(data['actions'])
    action = data['actions'][0]
    assert 'home' == action['name']
    assert 'safe' == action['type']
    assert 'test://home' == action['url']
    

