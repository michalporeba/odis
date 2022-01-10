from .descriptors import * 
from .docs import *

class Descriptor:
    def __init__(self, id: str, text: str=None, ref: str=None):
        self.id = id
        self.text = text 
        self.ref = ref 

    def to_data(self):
        data = {
            'id': self.id,
            'ref': 'https://schema.org/' + self.id
        }

        if self.text is not None: 
            data['text'] = self.text 
        
        if self.ref is not None: 
            data['ref'] = self.ref 
        
        return data 

class Safe(Descriptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_data(self):
        data = super().to_data()
        data['type'] = 'safe'
        return data

class Semantic(Descriptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_data(self):
        data = super().to_data()
        data['type'] = 'semantic'
        return data



class Alps(WithDocsMixin, DescriptorBase):
    def __init__(self, title: str=None, *args, **kwargs):
        super(Alps, self).__init__(*args, **kwargs)
        self.contents['version'] = '1.0'
        self.contents['title'] = title
        self.contents['descriptor'] = []
        self.init_docs()
        
    def to_data(self):
        data = super().to_data()
        return {
            'alps': data
        }

    def add(self, element: any) -> None: 
        if isinstance(element, Doc):
            self.add_doc(element)

        self.contents['descriptor'].append(element)
        return self

    def add_doc(self, doc: Doc):
        self.contents['doc'].append(doc)
        return self 