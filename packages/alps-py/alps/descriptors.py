from diogi.functions import *
from diogi.conventions import to_data
from .docs import WithDocsMixin

class Descriptor: 
    def parse(obj: any):
        if dict == type(obj):
            desc_type = get_if_exists(obj, 'type', 'semantic')
            docs = get_if_exists(obj, 'doc', None)

        else: 
            return None

        desc = None 

        if desc_type == 'semantic':
            desc = Semantic(
                id=get_if_exists(obj, 'id'),
                name=get_if_exists(obj, 'name')
            )

        if desc_type == 'safe':
            desc = Safe(
                id=get_if_exists(obj, 'id'), 
                name=get_if_exists(obj, 'name')
            )

        if docs: 
            add_doc = getattr(desc, 'add_doc', None) 
            if add_doc: 
                add_doc(docs)

        for d in always_a_list(get_if_exists(obj, 'descriptor', [])):
            desc.add_descriptor(d)

        return desc
 

class DescriptorBase(WithDocsMixin):
    def __init__(self):
        self.contents = {}

    @property
    def id(self):
        return get_if_exists(self.contents, 'id', None)

    @property 
    def name(self):
        return get_if_exists(self.contents, 'name', None)

    @property 
    def descriptors(self):
        return always_a_list(get_if_exists(self.contents, 'descriptor', []))

    def add_descriptor(self, descriptor: Descriptor):
        if not isinstance(descriptor, Descriptor):
            descriptor = Descriptor.parse(descriptor)

        append_if_not_none(self.contents, descriptor, 'descriptor')
        return self

    def get_descriptor(self, id: str) -> Descriptor:
        return list_is_optional([d for d in get_if_exists(self.contents, 'descriptor', []) if d.id == id])

    def as_data(self): 
        data = {}
        for k,v in self.contents.items():
            set_if_not_none(data, to_data(list_is_optional(v)), k)

        return data

    def __eq__(self, other):
        if type(other) is type(self):
            return self.contents == other.contents
        else:
            return False

    def __hash__(self):
        return hash((self.contents, self.contents))



class SimpleDescriptor(Descriptor, DescriptorBase):
    def __init__(self, 
        id: str, 
        text: str=None, 
        ref: str=None, 
        name: str=None,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.contents['id'] = id
        self.contents['text'] = text 
        self.contents['ref'] = ref 
        self.contents['name'] = name


class Safe(SimpleDescriptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contents['type'] = 'safe'


class Semantic(SimpleDescriptor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contents['type'] = 'semantic'
        