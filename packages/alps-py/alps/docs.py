class Doc:
    pass 

class MarkDownDoc(Doc):
    def __init__(self, value: str):
        self._value = value

    def to_data(self):
        return {
            'format': 'markdown',
            'value': self._value
        }