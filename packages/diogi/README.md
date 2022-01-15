# diog

Diog means to laze in Welsh. This package is to help me do less.

Most of the functions and decorators included in the `diog` package
could be easily implemented with a single line of obscure python
but then I would have to implement (and test) them again and again. 

I'd rather not. I'm lazy. 

## Functions

`always_a_list(obj: any) -> list` with alias `aal` 
takes any object and if it isn't a list already, it wraps it up in one.
It is also available as `@always_a_list` decorator. 

`default_if_none(obj: any, default: any) -> any:` with alias `din`
acts as a null coalescence.

`first_or_default(lst: list, default: any=None) -> any:` with alias `fod` returns the first element of a list
if there is at least one element, or the default value.

`get_if_exists(obj: any, key: str, default: any=None) -> any` with alias `gie`. 
attempts to get a property of a dictionary or an attribute of an object, and if it doesn't exist or is None the default value is returned.

`list_is_optional(obj: any) -> any` with alias `lio`
takes any object and if it is a list with a single element
then it returns just the element, otherwise the list is returned. 
It is also available as `@list_is_optional` decorator. 

`list_without_nones(lst: list) -> list` with alias `lwn`
returns copy of the list without any None values.
It is also available as `@list_without_nones` decorator. 

`none_if_empty(obj: any) -> any` with alias `nie`
returns copy of the object unless it is an empty list or an empty directory

`append_if_not_none(obj: any, value: any, key: str) -> any` with alias `ainn`

`get_if_exists(obj: any, key: str) -> any` with alias `gie`

`set_if_not_none(obj: any, value: any, key: str) -> any` with alias `sinn`

## Conventions

**to_data** sometimes the object needs to be converted to a simpler data
representation of dicts and lists. In those cases my objects implement 
a public method `as_data(self)`. The `diog.conventions.to_data(obj: any)` 
takes an object or a list of object, and reduces the input to data. 