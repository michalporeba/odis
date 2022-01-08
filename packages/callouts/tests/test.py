from types import FunctionType
from typing import Type


def query_first(func) -> callable:
    def wrapper():
        results = []
        for i in __class__.instances:
            fn = func.__name__
            if getattr(i, fn, None) \
                and not getattr(__class__, fn).__qualname__==getattr(i, fn).__qualname__:
                try:
                    results += __class__._always_array(getattr(i, fn)())
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
        cls._implementations = {}

        def _register_implementation(f: callable) -> None:
            name = f.__name__
            if name.startswith('_'):
                return

            print(f'adding {f.__qualname__} to {cls.__name__}')
            if f.__name__ not in cls._implementations.keys():
                cls._implementations[f.__name__] = [f]
                print('first registration')
            else:
                cls._implementations[f.__name__].append(f)
            
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.instances.append(cls())

            print('------------')
            for name in dir(cls):
                if not name.startswith('_'):
                    f = getattr(cls, name, None)
                    if type(f) == FunctionType: 
                        cls._register_implementation(f)
                        

        @staticmethod
        def _always_array(value: any) -> list:
            if type(value) == list:  
                return value
            else: 
                return [value]
        
    return CalloutsBase

def query_test(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        print()
        #return func()
    return wrapper



###################


@base
class APlugin:
    def get_name() -> list:
        pass


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
    def get_name() -> str:
        pass

class FirstB(BPlugin):
    def get_name(self):
        return 'b first'


print(APlugin._implementations)
print(APlugin.get_name())
#print(FirstA().get_name())