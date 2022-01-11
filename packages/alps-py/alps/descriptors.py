from diogi.functions import *
from diogi.conventions import to_data
from .docs import WithDocsMixin

class Descriptor: 
    pass 

class DescriptorBase(WithDocsMixin):
    def __init__(self):
        self.contents = {}

    def add_descriptor(self, descriptor: Descriptor):
        append_if_not_none(self.contents, descriptor, 'descriptor')
        return self

    def as_data(self): 
        data = {}
        for k,v in self.contents.items():
            set_if_not_none(data, to_data(list_is_optional(v)), k)

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
        