def to_data(obj: any) -> dict | list | None:
    """
    If the object passed as the argument of the function implements `as_data()`
    function then its return will be used, otherwise the object will be returned.
    If the input is a list, then the elements are processed following the above rules.
    The result must be a dictionary, a list of dictionaries or None
    """
    if obj is None:
        return None
    if list == type(obj):
        return [to_data(e) for e in obj]
    f = getattr(obj, "as_data", None)
    if f is not None:
        return f()
    return obj
