from .descriptors import DescriptorBase
from diogi.conventions import to_data

class Alps(DescriptorBase):
    def __init__(self, title: str=None, *args, **kwargs):
        super(Alps, self).__init__(*args, **kwargs)
        self.contents['version'] = '1.0'
        self.contents['title'] = title
        
    def as_data(self):
        return {
            'alps': to_data(super())
        }