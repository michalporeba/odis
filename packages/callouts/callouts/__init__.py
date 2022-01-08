def t(c, n):
    raise Exception('xxx')

def base(cls):
    class CalloutsBase(cls):
        cls.instances = []
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.instances.append(cls())
        def __getattribute__ (cls, name):
            print('XXXXX' + name)

        def query_first(func) -> callable:
            def wrapper():
                results = []
                for i in __class__.instances:
                    fn = func.__name__
                    if getattr(i, fn, None) \
                        and not getattr(__class__, fn).__qualname__==getattr(i, fn).__qualname__:
                        try:
                            results += __class__.accept(getattr(i, fn)())
                        except Exception as err:
                            print(err)
                            pass

                return results
            return wrapper 
        
    return CalloutsBase

def query_first(func: callable) -> callable:
    def wrapper():
        print(dir(func.__globals__.keys()))
        return func.__globals__.values
        
    return wrapper

def query_second(func: callable) -> callable:
    def wrapper():
        print(dir(func))
        return [func.__qualname__,
            func.__text_signature__
        ]
    return wrapper
