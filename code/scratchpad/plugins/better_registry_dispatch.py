from typing import Callable

class PluginBase:
    instances = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.instances.append(cls())

    def query(func: Callable) -> Callable:
        def wrapper():            
            results = []
            for i in PluginBase.instances:
                fn = func.__name__
                if getattr(i, fn, None) \
                    and not getattr(PluginBase, fn).__qualname__==getattr(i, fn).__qualname__:
                    try:
                        results += PluginBase.accept(getattr(i, fn)())
                    except Exception as err:
                        print(err)
                        pass

            return results

        return wrapper


    @staticmethod
    def accept(value: any) -> list:
        if type(value) == list:  
            return value
        else: 
            return [value]

    def dispatch() -> list: 
        results = []
        for i in PluginBase.instances:
            if getattr(i, 'dispatch', None) and not PluginBase.dispatch.__qualname__==i.dispatch.__qualname__:
                try:
                    results += PluginBase.accept(i.dispatch())
                except Exception as err:
                    print(err)
                    pass

        return results

    @query 
    def sample() -> list: 
        return []



class First(PluginBase):
    def dispatch(self) -> any:
        return 'from first'
    
    def sample(self) -> any: 
        return 'sample one'

class Second(PluginBase):
    def dispatch(self) -> any:
        return ['from second']

    def sample(self) -> any: 
        return 'sample two'

class Third(PluginBase):
    pass

    def sample(self) -> any:
        return 'sample three'

for p in PluginBase.sample():
    print(p)
