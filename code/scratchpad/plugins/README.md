# Scratchpad - Plugins

I want to avoid close coupling of the Data Exchange Network elements
with the framework in which it operates. It might be Django today, something else tomorrow. 

At the same time, I want to allow service developers to be able to easily 
adapt their solutions to join the network. Dependencies will be a barier for adoption. 

## Problems (with common solutions)

Python people do do much of dependency injection. DI Containers are not very popular. 

Strategy pattern could be an obvious pattern, but it could be difficult to implement
without some central DI Container. 

Pub/Sub communication is typically asynchronous, and there is no need or that level of complexity.
But it would allow for multiple registrations making the solution more flexible.


## Possible solution

**Registry** is a common pattern in Python. Since version 3.6 it is made easy 
by the [PEP 487](https://www.python.org/dev/peps/pep-0487) introduced
`__init__subclass` hook. 


```python
class PluginBase:
    subclasses = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
```

With this we can now define derived classes

```python
class PluginA(PluginBase):
    pass

class PluginB(PluginBase):
    pass
```

As soon as a extending type is defined - imported - it will be available in 
`PluginBase.subclasses` static list. 

**Dispatcher** pattern could be now used, to synchronously call methods of any existing implementation

```python
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
```

The result is this output: 
>hello from A<br />
>hello from B