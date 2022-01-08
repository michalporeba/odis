import callouts

##### SETUP #######

@callouts.base
class APlugin:
    def get_id() -> int: 
        return 0

    @callouts.first
    def get_name() -> str:
        pass

    def get_not_once_implemented() -> str:
        return 'default value'

    @callouts.flat 
    def get_many() -> list:
        pass

class FirstA(APlugin):
    def get_id() -> int:
        return 1

    def get_many() -> list:
        return [10, 11]

class SecondA(APlugin):
    def get_id() -> int:
        return 2

    def get_name() -> str:
        return 'a second'

    def get_many() -> list: 
        return 12

class ThirdA(APlugin):
    def get_id() -> int:
        return 3

    def get_name() -> str:
        return 'a thrid'

    def get_many() -> list: 
        return 'and more'

@callouts.base
class BPlugin:
    def get_id() -> int:
        pass 

    @callouts.first
    def get_name() -> str:
        pass

    @callouts.flat
    def do_your_maths(*args) -> list:
        pass

class FirstB(BPlugin):
    def get_id() -> int:
        pass 

    def get_name() -> str:
        return 'b first'

    def do_your_maths(*args):
        result = 0
        for a in args:
            result += a
        return result 

class SecondB(BPlugin):
    def get_id() -> int:
        pass 
    def get_name() -> str:
        return 'b second'
    def do_your_maths(*args):
        result = 1
        for a in args:
            result *= a 
        return result 


##### TESTS #######

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