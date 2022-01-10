# ALSP-PY

A python package to make implementing [Application-Level Profile Semantics (ALPS)](http://alps.io/) in projects. 

## Package Development

I am developing this package as part of work on the [Open Distributed Information Service (ODIS)](https://github.com/michalporeba/odis/).
Hopefully, it will be useful beyond this project, but I am not ready to make any promises just yet. 
At the moment it should be considered an experimental work.

## Related Work 

There is also the [WSTL-PY](https://pypi.org/project/wstl-py/) developed for the same reason, 
which helps with [Web Service Transition Language (WSTL)](http://rwcbook.github.io/wstl-spec/) implementations. 

## Feedback 

Any feedback will be welcomed. Create an issue, or start a discussion on the [ODIS repo](https://github.com/michalporeba/odis/)

&nbsp;
# Usage 

At the moment is is possible to create a valid ALPS representation from code:

```python
alps = Alps(title='Sample API')
alps.add_doc(MarkDownDoc('A sample MarkDown documentation'))
alsp.add_descriptor(Semantic(
    id='identifier', 
    text='An identifier of a thing',
    ref='https://schema.org/identifier'
))
alsp.add_descriptor(Semantic(
    id='email', 
    text='Email address for a person or an organisation',
    ref='https://schema.org/email'
))
print(alps.to_data())
```

and the output is

```javascript
{ 
    "alps": {
        "version": "1.0",
        "title": "Sample API",
        "doc": {
            "format": "markdown",
            "value": "A sample MarkDown documentation"
        },
        "descriptor": [
            { 
                "id": "identifier",
                "type": "semantic", 
                "text": "An identifier of a thing",
                "ref": "https://schema.org/identifier"
            },
            { 
                "id": "email",
                "type": "semantic", 
                "text": "Email address for a person or an organisation",
                "ref": "https://schema.org/identifier"
            }
        ]
    }
}
```

&nbsp;
# Plans

[ ] Abiility to read ALPS documents with validation
[ ] Standard descriptors from [Schema.org](https://schema.org/)
[ ] Integration with [WSTL-PY](https://pypi.org/project/wstl-py/) project