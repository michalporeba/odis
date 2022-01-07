class PluginBase:
    instances = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.instances.append(cls())

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

    


class First(PluginBase):
    def dispatch(self) -> any:
        return 'from first'

class Second(PluginBase):
    def dispatch(self) -> any:
        return ['from second']

class Third(PluginBase):
    pass

for p in PluginBase.dispatch():
    print(p)
