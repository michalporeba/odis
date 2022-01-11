from diogi.functions import *

class Doc:
    pass 

class WithDocsMixin:
    def __init__(self, *args, **kwargs):
        super(WithDocsMixin, self).__init__(*args, **kwargs)
    
    def add_doc(self, doc: Doc):
        append_if_not_none(self.contents, doc, 'doc')
        return self

class MarkDownDoc(Doc):
    def __init__(self, value: str):
        self.value = value

    def as_data(self):
        return {
            'format': 'markdown',
            'value': self.value
        }