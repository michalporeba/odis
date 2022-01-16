from diogi.decorators import *


def test_always_a_list_wrapper():
    @always_a_list
    def test(obj: any) -> any:
        return obj

    assert [None] == test(None)
    assert [None] == test([None])
    assert [1, 2, 3] == test([1, 2, 3])


def test_first_or_default_wrapper():
    @first_or_default(None)
    def test_default_default(obj: any) -> any:
        return obj

    @first_or_default(9)
    def test_custom_default(obj: any) -> any:
        return obj

    assert test_default_default([]) is None
    assert test_default_default(None) is None
    assert 9 == test_custom_default([])
    assert 9 == test_custom_default(None)
    assert 1 == test_custom_default([1, 2])


def test_list_is_optional_wrapper():
    @list_is_optional
    def test(obj: any) -> any:
        return obj

    assert test(None) is None
    assert test([]) is None
    assert test([None]) is None
    assert 1 == test(1)
    assert 1 == test([1])
    assert [1, 2] == test([1, 2])


def test_list_without_nones():
    @list_without_nones
    def test(lst: list) -> list:
        return lst

    assert [] == test([])
    assert [] == test([None])
    assert [] == test([None, None])
    assert [2, 4] == test([None, 2, None, 4, None])
