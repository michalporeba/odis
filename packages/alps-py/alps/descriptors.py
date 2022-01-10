from .utils import *

class DescriptorBase:
    def __init__(self):
        self.contents = {}

    def to_data(self): 
        print('base to_data')
        print(self.contents)
        data = {}
        for k,v in self.contents.items():
            print(f'{k} -> {v}')
            ade(data, k, dol(v))

        return data