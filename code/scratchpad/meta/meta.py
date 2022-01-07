
from types import FunctionType


def decorator(cls):
    class NewClass(cls):
        attr = 100
        cls.s = 'static'
    return NewClass

@decorator 
class A:
    pass

@decorator 
class B:
    pass 

a = A()

print(a.attr)
A.s = 'hello'
print(A.s)
print(B.s)


def deco(func: FunctionType) -> FunctionType:
    def wrap():
        print('before')
        func()
        print('after')
        print(func.__name__)
    return wrap

@deco
def test():
    print('test')

print ('-------------')

test()