class MarkDownDoc():
    def __init__(self, text: str):
        self._text = text        

    def to_data(self):
        return {
            'type': 'markdown',
            'value': self._text
        }

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
        self._doc = None
        self._descriptors = []

    def to_data(self):
        data = {
            'version': self._version
        }

        if self._title is not None:
            data['title'] = self._title

        if self._doc is not None:
            data['doc'] = self._doc.to_data()

        if len(self._descriptors) == 1:
            data['descriptor'] = self._descriptors[0].to_data()

        return {
            'alps': data
        }

    def add(self, descriptor: Descriptor) -> None: 
        self._descriptors.append(descriptor)
        return self

    def with_markdown_doc(self, doc: MarkDownDoc):
        self._doc = doc
        return self 