from diogi.aliases import *


def test_append_if_not_none_on_dictionary():
    d = {}
    ainn(d, None, "key")
    assert 0 == len(d.keys())
    c = ainn(d, 1, "key")
    assert d["key"] == [1]
    assert c["key"] == [1]
    ainn(d, 2, "key")
    assert d["key"] == [1, 2]


def test_append_if_not_none_on_list():
    lst = []
    ainn(lst, None)
    assert 0 == len(lst)
    c = ainn(lst, "a")
    assert ["a"] == c


def test_always_a_list_function():
    assert [None] == aal(None)
    assert [None] == aal([None])
    assert [1, 2, 3] == aal([1, 2, 3])


def test_default_if_none():
    assert 1 == din(1, 2)
    assert 2 == din(None, 2)


def test_first_or_default():
    assert fod([]) is None
    assert fod(None) is None
    assert 9 == fod([], 9)
    assert 9 == fod(None, 9)
    assert 1 == fod([1, 2], 9)


def test_get_if_exists():
    class T:
        def __init__(self):
            self.value = 123

        property = "abc"

    assert gie(None, None) is None
    assert gie({}, None) is None
    assert gie(None, "test") is None
    assert gie({"a": 1}, "test") is None
    assert 3 == gie({"test": 3}, "test")
    assert "abc" == gie(T, "property")
    assert 123 == gie(T(), "value")


def test_get_if_exists_with_default():
    class T:
        def __init__(self):
            self.value = 123

        property = "abc"

    assert "a" == gie(None, None, "a")
    assert "b" == gie({}, None, "b")
    assert "c" == gie(None, "key", "c")
    assert "d" == gie({"a": 2}, "wrong", "d")

    assert 123 == gie(T(), 'value')
    assert 'abc' == gie(T, 'property')


def test_list_is_optional_function():
    assert lio(None) is None
    assert lio([]) is None
    assert lio([None]) is None
    assert 1 == lio(1)
    assert 1 == lio([1])
    assert [1, 2] == lio([1, 2])


def test_list_without_nones():
    assert [] == lwn([])
    assert [] == lwn([None])
    assert [] == lwn([None, None])
    assert [2, 4] == lwn([None, 2, None, 4, None])


def test_none_if_empty():
    assert [1] == nie([1])
    assert [1, 2] == nie([1, 2])
    assert nie([]) is None
    assert nie({}) is None


def test_set_if_not_none_on_dictionary():
    d = {}
    sinn(d, None, "x")
    assert "x" not in d.keys()
    sinn(d, 2, "a")
    assert d["a"] == 2
    assert sinn(d, 5, "b")["b"] == 5


def test_set_if_not_none_on_list():
    lst = []
    assert ["a"] == sinn(lst, "a")
    assert ["a"] == sinn(lst, None)
    assert ["a", "b"] == sinn(lst, "b")
