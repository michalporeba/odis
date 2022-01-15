import logging 
from .descriptors import DescriptorBase
from diogi.conventions import to_data
from diogi.functions import get_if_exists, always_a_list

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

        data = obj['alps']
        version = get_if_exists(data, 'version', '1.0')
        if (version != '1.0'): 
            logger.warning(f'The document is in unsupported ALPS version {version}')

        alps = Alps(version=version)
        alps.set_title(get_if_exists(data, 'title', None))

        for d in always_a_list(get_if_exists(data, 'doc', [])):
            alps.add_doc(d)

        for d in always_a_list(get_if_exists(data, 'descriptor', [])):
            alps.add_descriptor(d)

        return alps