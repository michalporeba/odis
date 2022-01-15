from alps.descriptors import *

def test_descriptors_are_semantic_by_default():
    desc = Descriptor.parse({'id': 'sample'})
    assert Semantic(id='sample') == desc