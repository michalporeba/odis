from diogi.decorators import *

def test_always_a_list_wrapper():
    @always_a_list 
    def test(obj: any) -> any: 
        return obj 

    assert [None] == test(None)
    assert [None] == test([None])
    assert [1,2,3] == test([1,2,3])

def test_list_is_optional_wrapper():
    @list_is_optional
    def test(obj: any) -> any:
        return obj

    assert None == test(None)
    assert None == test([])
    assert None == test([None])
    assert 1 == test(1)
    assert 1 == test([1])
    assert [1,2] == test([1,2])


def test_list_without_nones():
    @list_without_nones
    def test(lst: list) -> list:
        return lst

    assert [] == test([])
    assert [] == test([None])
    assert [] == test([None,None])
    assert [2,4] == test([None,2,None,4,None])
