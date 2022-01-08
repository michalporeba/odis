class PluginBase:
    instances = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.instances.append(cls())

    def hello() -> list:
        results = []
        for i in PluginBase.instances:
            results.append(i.hello())
        return results

class PluginA(PluginBase):
    def hello(self) -> str:
        return "hello from A"

class PluginB(PluginBase):
    def hello(self) -> str:
        return "hello from B"

for p in PluginBase.hello():
    print(p)


print('----------------------SECOND EXPERIMENT--------')

class FancyPluginBase:
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

    def dispatch(type: any = None) -> list: 
        return [r for i in FancyPluginBase.instances for r in FancyPluginBase.accept(i.respond_to(type))]

    def respond_to(self, type: any = None) -> any:
        return []
    


class First(FancyPluginBase):
    def respond_to(self, type: any = None) -> any:
        return 'from first'

class Second(FancyPluginBase):
    def respond_to(self, type: any = None) -> any:
        return ['from second']

class Third(FancyPluginBase):
    pass


for p in FancyPluginBase.dispatch():
    print(p)


