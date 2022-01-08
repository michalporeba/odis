def base(decorator):
    class 

###################


@base
class APlugin:
    @query_test
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

@base
class BPlugin:
    @query_test 
    def get_name() -> str:
        pass

class FirstB(BPlugin):
    def get_name(self):
        return 'b first'


APlugin.get_name()