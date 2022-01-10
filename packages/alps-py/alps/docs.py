class Doc:
    pass 

class WithDocsMixin:
    def __init__(self, *args, **kwargs):
        super(WithDocsMixin, self).__init__(*args, **kwargs)
    
    def init_docs(self):
        self.contents['doc'] = []

class MarkDownDoc(Doc):
    def __init__(self, value: str):
        self.value = value

    def to_data(self):
        return {
            'format': 'markdown',
            'value': self.value
        }