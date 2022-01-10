# WSTL-PY

A python package to make implementing [Web Service Transition Language (WSTL)](http://rwcbook.github.io/wstl-spec/) in projects. 

## Package Development

I am developing this package as part of work on the [Open Distributed Information Service (ODIS)](https://github.com/michalporeba/odis/). 
Hopefully, it will be useful beyond this project, but I am not ready to make any promises just yet. 
At the moment it should be considered an experimental work.

## Related Work 

There is also the [ALPS-PY](https://pypi.org/project/alps-py) developed for the same reason, 
which helps with [Application-Level Profile Semantics (ALPS)](http://alps.io/) implementations. 

## Feedback 

Any feedback will be welcomed. Create an issue, or start a discussion on 
the [ODIS repo](https://github.com/michalporeba/odis/)

&nbsp;
# Usage 

At the moment it is possible to create a valid WSTL message from code: 

```python
wstl = Wstl()
wstl.add_action(...)
wstl.add_data_item(...)

print(wstl.to_data())
```

Behind the scenes it can resolve action names to full action descriptions. 

&nbsp;
# Plans

[ ] Integration with [ALPS-PY](https://pypi.org/project/alps-py) project