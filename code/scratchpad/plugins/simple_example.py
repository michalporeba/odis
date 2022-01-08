class PluginBase:
    instances = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.instances.append(cls())

    def query(func: callable) -> callable:
        def wrapper():            
            results = []
            for i in PluginBase.instances:
                fn = func.__name__
                if getattr(i, fn, None) \
                    and not getattr(PluginBase, fn).__qualname__==getattr(i, fn).__qualname__:
                    try:
                        results += PluginBase.always_array(getattr(i, fn)())
                    except Exception as err:
                        print(err)
                        pass

            return results

        return wrapper

    @staticmethod
    def always_array(value: any) -> list:
        if type(value) == list:  
            return value
        else: 
            return [value]

    @query 
    def options() -> list: 
        return []


class First(PluginBase):
    def options(self) -> any:
        return 'from first'
    
class Second(PluginBase):
    def options(self) -> any:
        return ['from second']

print(PluginBase.options())
