from types import FunctionType
            
def _query_all_wrapper(functions: list) -> any:
    def wrapper(*args, **kwargs):
        return [f(*args, **kwargs) for f in functions]
    return wrapper

def _get_first_wrapper(functions: list) -> any:
    def wrapper(*args, **kwargs):
        if len(functions) > 0:
            return functions[0](*args, **kwargs)
    return wrapper

def _get_flat_wrapper(functions: list) -> any:
    def wrapper(*args, **kwargs):
        results = []
        for v in [f(*args, **kwargs) for f in functions]:
            if type(v) == list: 
                results += v
            else:
                results += [v]
        return results
    return wrapper

def _wrap(cls, name):
    template = getattr(cls, name, None)
    callout_mode = getattr(template, '_callouts_mode', 'query_all')

    if callout_mode == 'first':
        setattr(cls, name, _get_first_wrapper(cls._implementations[name]))
    elif callout_mode == 'flat':
        setattr(cls, name, _get_flat_wrapper(cls._implementations[name]))
    else:
        setattr(cls, name, _query_all_wrapper(cls._implementations[name]))
        
### decorators

def first(func: callable) -> any: 
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    setattr(wrapper, '_callouts_mode', 'first')
    return wrapper
    
def flat(func: callable) -> any: 
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    setattr(wrapper, '_callouts_mode', 'flat')
    return wrapper

def base(cls):
    def _private_or_internal(f: callable) -> bool:
        return f.__name__.startswith('_')

    def _is_the_template(f: callable) -> bool:
        return f.__qualname__.startswith(cls.__name__+'.')

    def _there_is_no_template(f: callable) -> bool: 
        return getattr(cls, f.__name__, None) is None 

    def _find_all_methods(obj: any) -> list: 
        attributes = [getattr(obj, a) for a in dir(obj)]
        return [a for a in attributes if type(a) == FunctionType]

    class CalloutsBase(cls):
        cls._implementations = {}

        def _register_implementation(f: callable) -> None:
            if _private_or_internal(f) \
                or _is_the_template(f) \
                or _there_is_no_template(f): 
                return 

            if f.__name__ not in cls._implementations.keys():
                template = getattr(cls, f.__name__, None)
                # don't register methods that are not defined on plugin base
                if template is not None: 
                    cls._implementations[f.__name__] = [f]
                    _wrap(cls, f.__name__)
            else:
                cls._implementations[f.__name__].append(f)
            
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            for m in _find_all_methods(cls):
                cls._register_implementation(m)
                        
    return CalloutsBase


