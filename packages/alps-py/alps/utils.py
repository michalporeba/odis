def dol(obj: any) -> map|list: 
    """
    returns a dictionary if a dictionary or a list with just one item is provided
    returns None if None is given, or an empty list
    returns a list otherwise
    """
    if list == type(obj):
        if len(obj) == 0:
            return None
        elif len(obj) == 1:
            return obj[0]
    return obj

def to_data(obj: any) -> any: 
    if obj == None: 
        return None
    if list == type(obj):
        return [to_data(e) for e in obj if e is not None]
    f = getattr(obj, 'to_data', None)
    if f is not None:
        print(f'executing to_data on {obj}')
        return f()
    return obj

def ade(dictionary: dict, key: str, source: any) -> dict:
    data = to_data(source)
    if data is not None: 
        dictionary[key] = data
    return dictionary