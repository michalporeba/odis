def f(obj: any):
    if list == type(obj):
        return [f(i) for i in obj]
    return obj+1 
