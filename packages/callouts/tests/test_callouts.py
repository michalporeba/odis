from .sample.aplugin import APlugin
from .sample.apluginimpl import *
from .sample.bplugin import BPlugin
from .sample.bpluginimpl import *


def test_query_first_in_a():
    assert 'a second' == APlugin.get_name()

def test_query_first_in_b():
    assert 'b first' == BPlugin.get_name()

def test_return_default_value_if_not_implemented():
    assert 'default value' == APlugin.get_not_once_implemented()

def test_return_all_in_a():
    assert [1,2,3] == APlugin.get_id()
    
def test_return_all_in_b():
    assert [None, None] == BPlugin.get_id()

def test_return_many_in_a():
    assert [10, 11, 12, 'and more'] == APlugin.get_many()

def test_parameter_passing():
    assert [9, 24] == BPlugin.do_your_maths(2,3,4)