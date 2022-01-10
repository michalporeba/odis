from .descriptors import Descriptor, DescriptorBase
from .docs import Doc

class Alps(DescriptorBase):
    def __init__(self, title: str=None, *args, **kwargs):
        super(Alps, self).__init__(*args, **kwargs)
        self.contents['version'] = '1.0'
        self.contents['title'] = title
        
    def to_data(self):
        return {
            'alps': super().to_data()
        }