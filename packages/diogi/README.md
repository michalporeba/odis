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

`list_is_optional(obj: any) -> any` with alias `lio`
takes any object and if it is a list with a single element
then it returns just the element, otherwise the list is returned. 
It is also available as `@list_is_optional` decorator. 

`list_without_nones(lst: list) -> list` with alias `lwn`
returns copy of the list without any None values.
It is also available as `@list_without_nones` decorator. 

## Conventions

**to_data** sometimes the object needs to be converted to a simpler data
representation of dicts and lists. In those cases my objects implement 
a public method `to_data(self)`. The `diog.conventions.to_data(obj: any)` 
takes an object or a list of object, and reduces the input to data. 