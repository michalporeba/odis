
from ..callouts import * 

@callouts.base
class APlugin:
    @callouts.query_first
    def get_name() -> str:
        return ''

    def __init__(self):
        self.a = 'x'

class FirstA(APlugin):
    pass 

class SecondA(APlugin):
    def get_name(self):
        return 'a second'

class ThirdA(APlugin):
    def get_name(self):
        return 'a thrid'

@callouts.base
class BPlugin:
    pass

class FirstB(BPlugin):
    def get_name(self):
        return 'b first'

def test_query_first_in_a():
    assert 'a second' == APlugin.get_name()
    assert 'b' == a.a

APlugin.get_name()