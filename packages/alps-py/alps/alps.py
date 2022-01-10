from .descriptors import Descriptor, DescriptorBase
from .docs import Doc, WithDocsMixin

class Alps(WithDocsMixin, DescriptorBase):
    def __init__(self, title: str=None, *args, **kwargs):
        super(Alps, self).__init__(*args, **kwargs)
        self.contents['version'] = '1.0'
        self.contents['title'] = title
        
    def to_data(self):
        return {
            'alps': super().to_data()
        }

    def add(self, element: any) -> None: 
        if isinstance(element, Doc):
            self.add_doc(element)
        if isinstance(element, Descriptor):
            self.add_descriptor(element)
        return self
