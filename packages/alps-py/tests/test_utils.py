from alps.utils import *

class WithoutToData:
    def __init__(self, x:int):
        self.x = x
class WithToData:
    def __init__(self, x:int):
        self.x = x 
    def to_data(self):
        return self.x+self.x
        
def test_dict_or_list():
    assert None == dol(None)
    assert None == dol([])
    assert None == dol([None])
    assert 1 == dol(1)
    assert 1 == dol([1])
    assert [1,2] == dol([1,2])
    
def test_to_data():
    

    assert None == to_data(None)
    assert 1 == to_data(1)
    assert [1,2] == to_data([1,2])
    assert [2,4] == to_data([WithToData(1), WithToData(2)])
    assert to_data(WithoutToData(10)).x == 10
    assert [1,3] == to_data([1,None,3,None])

def test_add_data_element():
    d = {}
    ade(d, 't1', [1,2,3])
    ade(d, 't2', WithToData(3))
    ade(d, 't3', [WithToData(3), WithToData(4)])
    assert [1,2,3] == d['t1']
    assert 6 == d['t2']
    assert [6, 8] == d['t3']