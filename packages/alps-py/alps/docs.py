class Doc:
    pass 

class WithDocsMixin:
    def __init__(self, *args, **kwargs):
        super(WithDocsMixin, self).__init__(*args, **kwargs)
    
    def add_doc(self, doc: Doc):
        if 'doc' not in self.contents.keys():
            self.contents['doc'] = []
        self.contents['doc'].append(doc)
        return self

class MarkDownDoc(Doc):
    def __init__(self, value: str):
        self.value = value

    def to_data(self):
        return {
            'format': 'markdown',
            'value': self.value
        }