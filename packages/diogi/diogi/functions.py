def append_if_not_none(obj: any, value: any, key: str = None) -> any:
    if value is None:
        return obj

    if key is None and list == type(obj):
        obj.append(value)

    if key is not None and dict == type(obj):
        if key not in obj.keys():
            obj[key] = []
        obj[key].append(value)

    return obj


def always_a_list(obj: any) -> list:
    """
    returns a list no matter what is in the input.
    if the argument is a list already it gets returned verbatim
    but if it is not, it is wrapped into a list
    """
    if list == type(obj):
        return obj
    else:
        return [obj]


def default_if_none(obj: any, default: any) -> any:
    if obj is None:
        return default
    return obj


def first_or_default(lst: list | None, default: any = None) -> any:
    if lst is None:
        return default
    if list == type(lst):
        if 0 == len(lst):
            return default
        else:
            return lst[0]
    return None


def get_if_exists(obj: any, key: str | None, default: any = None) -> any:
    if obj is None or key is None:
        return default

    if dict == type(obj):
        if key in obj.keys():
            return obj[key]
        else:
            return default

    attr = getattr(obj, key, default)
    return attr


def list_is_optional(obj: any) -> any:
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


def list_without_nones(lst: list) -> list:
    return [e for e in lst if e is not None]


def none_if_empty(obj: any) -> any:
    if list == type(obj) and len(obj) == 0:
        return None
    if dict == type(obj) and len(obj.keys()) == 0:
        return None
    return obj


def set_if_not_none(obj: any, value: any, key: str = None) -> any:
    if value is None:
        return obj

    if key is None and list == type(obj):
        obj.append(value)

    if key is not None and dict == type(obj):
        obj[key] = value

    return obj
