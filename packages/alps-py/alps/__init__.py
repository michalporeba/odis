from .utils import dol, to_data
from .docs import Doc

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

class Alps:
    def __init__(self, title: str=None):
        self._version = '1.0'
        self._title = title
        self._docs = []
        self._descriptors = []

    def to_data(self):
        data = {
            'version': self._version
        }

        if self._title is not None:
            data['title'] = self._title

        if len(self._docs) > 0:
            data['doc'] = to_data(dol(self._docs[0]))

        if len(self._descriptors) > 0:
            data['descriptor'] = to_data(dol(self._descriptors))
        
        return {
            'alps': data
        }

    def add(self, element: any) -> None: 
        if isinstance(element, Doc):
            self.add_doc(element)

        self._descriptors.append(element)
        return self

    def add_doc(self, doc: Doc):
        self._docs.append(doc)
        return self 