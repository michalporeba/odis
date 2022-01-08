from types import FunctionType
    
def _query_all_wrapper(functions: list) -> any:
    def wrapper(*args, **kwargs):
        return [f() for f in functions]
    return wrapper

def _get_first_wrapper(functions: list) -> any:
    def wrapper(*args, **kwargs):
        if len(functions) > 0:
            return functions[0]()
    return wrapper

def get_first(func: callable) -> any: 
    def wrapper(*args, **kwargs):
        func()
    setattr(wrapper, '_callouts_mode', 'first')
    return wrapper

def _wrap(cls, name):
    template = getattr(cls, name, None)
    callout_mode = getattr(template, '_callouts_mode', 'query_all')

    if callout_mode == 'first':
        setattr(cls, name, _get_first_wrapper(cls._implementations[name]))
    else:
        setattr(cls, name, _query_all_wrapper(cls._implementations[name]))
        
    
def base(cls):
    class CalloutsBase(cls):
        cls._instances = []
        cls._implementations = {}

        def _register_implementation(f: callable) -> None:
            name = f.__name__
            if name.startswith('_'):
                return

            if f.__qualname__.startswith(cls.__name__+'.'):
                return 

            base_function = getattr(cls, name, None)
            if base_function is None: 
                return 

            print(f'adding {f.__qualname__} to {cls.__name__}')
            if f.__name__ not in cls._implementations.keys():
                cls._implementations[f.__name__] = [f]
                print('first registration')
                _wrap(cls, name)
                print(getattr(cls, name, None))
                print(getattr(getattr(cls, name, None), 'purpose', 'none'))
            else:
                cls._implementations[f.__name__].append(f)
            
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls._instances.append(cls())

            print(f'------------{cls.__name__}')
            for name in dir(cls):
                if not name.startswith('_'):
                    f = getattr(cls, name, None)
                    if type(f) == FunctionType: 
                        cls._register_implementation(f)
                        

        @staticmethod
        def _always_array(value: any) -> list:
            if type(value) == list:  
                return value
            else: 
                return [value]
        
    return CalloutsBase

def query_test(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        print()
        #return func()
    setattr(wrapper, 'purpose', 'xxx')
    return wrapper


