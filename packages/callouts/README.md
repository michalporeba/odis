# Callouts 

A minimalist dispatch system for python module lose coupling. 

Imagine we had an application that checks weather for one place, but using multiple service. The functionality to get weather for a specific service could be implemented in individual modules. 

To implement this with `callouts`, we first need to implement the extensibility base by creating a class with the `@callouts.base` decorator. 

```python
@callouts.base
class Weather:
    def get_for(location: str) -> str: 
        pass 
```

Now, individual implementations can be added
simply by extending the class and implementing the `get_for` method. 

```python
class FirstWeatherService(Weather):
    def get_for(location: str) -> str: 
        return 'sunny' 
```

```python
class SecondWeatherService(Weather):
    def get_for(location: str) -> str: 
        return 'cloudy'
```

with those definition in place, as soon as the modes are loaded it is possible to get both weathers by calling the `get_for` method on the `Weather` class: 

```python
print(Weather.get_for('place'))
```
will print out 
```javascript
['sunny', 'cloudy']
```