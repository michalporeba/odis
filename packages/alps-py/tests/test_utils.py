from alps.utils import *

def test_dict_or_list():
    assert None == dol(None)
    assert None == dol([])
    assert None == dol([None])
    assert 1 == dol(1)
    assert 1 == dol([1])
    assert [1,2] == dol([1,2])
    
def test_to_data():
    class TestWithoutToData:
        def __init__(self, x:int):
            self.x = x
    class TestWithToData:
        def __init__(self, x:int):
            self.x = x 
        def to_data(self):
            return self.x+self.x

    assert None == to_data(None)
    assert 1 == to_data(1)
    assert [1,2] == to_data([1,2])
    assert [2,4] == to_data([TestWithToData(1), TestWithToData(2)])
    assert to_data(TestWithoutToData(10)).x == 10
