from types import FunctionType


def query_first(func) -> callable:
    def wrapper():
        results = []
        for i in __class__.instances:
            fn = func.__name__
            if getattr(i, fn, None) \
                and not getattr(__class__, fn).__qualname__==getattr(i, fn).__qualname__:
                try:
                    results += __class__.always_array(getattr(i, fn)())
                except Exception as err:
                    print(err)
                    pass

        return results
    return wrapper 
    
def t(c, n):
    raise Exception('xxx')

def base(cls):
    class CalloutsBase(cls):
        cls.instances = []
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.instances.append(cls())

        def __new__(cls):
            print('instantiating ' + str(cls.__name__))
            for name in dir(cls):
                if not name.startswith('_'):
                    f = getattr(cls, name, None)
                    if type(f) == FunctionType: 
                        purpose = getattr(f, 'purpose', 'none')
                        print(f' {name} -> {purpose}')
                        
                    #print(f' {name} {getattr(cls[name], 'purpose', 'none at all'))
                    
            return super(CalloutsBase, cls).__new__(cls)

        @staticmethod
        def always_array(value: any) -> list:
            if type(value) == list:  
                return value
            else: 
                return [value]
        
    return CalloutsBase

def query_test(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        func.purpose = 'just testing'
    return wrapper



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