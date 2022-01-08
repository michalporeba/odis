import callouts

##### SETUP #######

@callouts.base
class APlugin:
    def get_id() -> int: 
        return 0

    @callouts.get_first
    def get_name() -> str:
        pass

    def get_not_once_implemented() -> str:
        return 'default value'

class FirstA(APlugin):
    def get_id() -> int:
        return 1

class SecondA(APlugin):
    def get_id() -> int:
        return 2

    def get_name() -> str:
        return 'a second'

class ThirdA(APlugin):
    def get_id() -> int:
        return 3

    def get_name() -> str:
        return 'a thrid'

@callouts.base
class BPlugin:
    def get_id() -> int:
        pass 

    @callouts.get_first
    def get_name() -> str:
        pass

class FirstB(BPlugin):
    def get_id() -> int:
        pass 

    def get_name() -> str:
        return 'b first'

class SecondB(BPlugin):
    def get_id() -> int:
        pass 
    def get_name() -> str:
        return 'b second'



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