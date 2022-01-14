import logging 
from .descriptors import DescriptorBase
from diogi.conventions import to_data

logger = logging.getLogger(__name__)

class Alps(DescriptorBase):
    """
    Root ALPS Descriptor
    """
    def __init__(self, version: str='1.0', *args, **kwargs):
        super(Alps, self).__init__(*args, **kwargs)
        self.contents['version'] = version
        self.contents['title'] = None
        
    @property
    def version(self):
        return self.contents['version']

    @property 
    def title(self):
        return self.contents['title']

    def set_title(self, title: str):
        self.contents['title'] = title

    def as_data(self):
        return { 'alps': to_data(super()) }


    def parse(obj: dict): 
        if obj is None or \
            not dict == type(obj) or \
            not 'alps' in obj.keys():
            logger.warning('The document provided does not contain ALPS definition!')
        return Alps(version=None)
