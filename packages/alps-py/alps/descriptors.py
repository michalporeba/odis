from .utils import *
from .docs import WithDocsMixin

class Descriptor: 
    pass 

class DescriptorBase(WithDocsMixin):
    def __init__(self):
        self.contents = {}

    def add_descriptor(self, descriptor: Descriptor):
        if 'descriptor' not in self.contents.keys():
            self.contents['descriptor'] = []
        self.contents['descriptor'].append(descriptor)
        return self

    def to_data(self): 
        data = {}
        for k,v in self.contents.items():
            ade(data, k, dol(v))

        return data


class SimpleDescriptor(Descriptor, DescriptorBase):
    def __init__(self, id: str, text: str=None, ref: str=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contents['id'] = id
        self.contents['text'] = text 
        self.contents['ref'] = ref 


class Safe(SimpleDescriptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contents['type'] = 'safe'


class Semantic(SimpleDescriptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contents['type'] = 'semantic'
        