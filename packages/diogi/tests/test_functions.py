from diogi.aliases import *

def test_add_if_not_none():
    d = {}
    ainn(d, None, 'x')
    assert 'x' not in d.keys()
    ainn(d, 2, 'a')
    assert d['a'] == 2
    assert ainn(d, 5, 'b')['b'] == 5

    l = []
    assert ['a'] == ainn(l, 'a')
    assert ['a'] == ainn(l, None)
    assert ['a','b'] == ainn(l, 'b')

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