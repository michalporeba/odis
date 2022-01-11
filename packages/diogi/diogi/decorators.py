import diogi.functions as f

def always_a_list(func: callable) -> callable: 
    def wrapper(*args, **kwargs):
        return f.always_a_list(func(*args, **kwargs))
    return wrapper 

def list_is_optional(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        return f.list_is_optional(func(*args, **kwargs))
    return wrapper 

def list_without_nones(func: callable) -> callable: 
    def wrapper(*args, **kwargs):
        return f.list_without_nones(func(*args, **kwargs))
    return wrapper