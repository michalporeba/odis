from diogi.aliases import *

def test_append_if_not_none_on_dictionary():
    d = {}
    ainn(d, None, 'key')
    assert 0 == len(d.keys())
    c = ainn(d, 1, 'key')
    assert d['key'] == [1]
    assert c['key'] == [1]
    ainn(d, 2, 'key')
    assert d['key'] == [1,2]

def test_append_if_not_none_on_list():
    l = []
    ainn(l, None)
    assert 0 == len(l)
    c = ainn(l, 'a')
    assert ['a'] == c

def test_always_a_list_function():
    assert [None] == aal(None)
    assert [None] == aal([None])
    assert [1,2,3] == aal([1,2,3])

def test_list_is_optional_function():
    assert None == lio(None)
    assert None == lio([])
    assert None == lio([None])
    assert 1 == lio(1)
    assert 1 == lio([1])
    assert [1,2] == lio([1,2])

def test_list_without_nones():
    assert [] == lwn([])
    assert [] == lwn([None])
    assert [] == lwn([None,None])
    assert [2,4] == lwn([None,2,None,4,None])

def test_set_if_not_none_on_dictionary():
    d = {}
    sinn(d, None, 'x')
    assert 'x' not in d.keys()
    sinn(d, 2, 'a')
    assert d['a'] == 2
    assert sinn(d, 5, 'b')['b'] == 5

def test_set_if_not_none_on_list():
    l = []
    assert ['a'] == sinn(l, 'a')
    assert ['a'] == sinn(l, None)
    assert ['a','b'] == sinn(l, 'b')