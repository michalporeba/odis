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




