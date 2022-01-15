import pytest
from alps.descriptors import *

def noop_resolver(href: str):
    pass

def demo_resolver(href: str):
    if href != '#demo':
        raise Exception('this resolver expect #demo href to be provided')

    return {
        'id': 'resolved.id',
        'type': 'safe',
        'name': 'resolved.name'
    }

def test_descriptors_are_semantic_by_default():
    desc = Descriptor.parse({'id': 'sample'}, noop_resolver)
    assert Semantic(id='sample') == desc

def test_resolver_getting_href():
    with pytest.raises(Exception):
        Descriptor.parse({'href': 'unsupported_href'}, demo_resolver)

def test_resolving():
    desc = Descriptor.parse({'href': '#demo'}, demo_resolver)
    assert 'resolved.id' == desc.id
    assert Safe == type(desc)
    assert 'resolved.name' == desc.name

    desc = Descriptor.parse({'href': '#demo', 'id': 'my.id'}, demo_resolver)
    assert 'my.id' == desc.id
    assert Safe == type(desc)
    assert 'resolved.name' == desc.name

    desc = Descriptor.parse({'href': '#demo', 'type': 'semantic', 'name': 'hello'}, demo_resolver)
    assert 'resolved.id' == desc.id
    assert Semantic == type(desc)
    assert 'hello' == desc.name
