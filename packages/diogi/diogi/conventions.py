def to_data(obj: any) -> dict|list:
    if obj == None: 
        return None
    if list == type(obj):
        return [to_data(e) for e in obj]
    f = getattr(obj, 'as_data', None)
    if f is not None:
        return f()
    return obj