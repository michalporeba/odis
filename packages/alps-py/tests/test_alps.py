import pytest
from alps import *
from alps.docs import *

def test_root_is_alps():
    root = Alps().to_data()
    assert 1 == len(root.keys())
    assert None != root['alps']

def test_version_defaults_to_one():
    data = Alps().to_data()['alps']
    assert '1.0' == data['version']

@pytest.mark.parametrize('attribute', ['title', 'doc', 'descriptor'])
def test_there_are_no_unnecessary_attributes_by_default(attribute: str):
    data = Alps().to_data()['alps']
    assert attribute not in data.keys()

@pytest.mark.parametrize('alps_title', ['Sample API', 'Another API'])
def test_title_from_constructor(alps_title: str):
    data = Alps(alps_title).to_data()['alps']
    assert alps_title == data['title']
@pytest.mark.parametrize('text', ['abc', 'def'])
def test_markdown_documentation(text: str):
    data = Alps().\
        add(MarkDownDoc(text)).\
        to_data()['alps']
    assert 'markdown' == data['doc']['format']
    assert text == data['doc']['value']

@pytest.mark.parametrize('id,text,ref', [
    ('identifier', 'Unique Identifier', 'https://schema.org/identifier'),
    ('email', 'Test email address', 'https://schema.org/email')
])
def test_single_semantic_descriptor(id, text, ref):
    alps = Alps()
    alps.add(Semantic(id=id, text=text))
    data = alps.to_data()['alps']['descriptor']
    print(data)
    assert 'semantic' == data['type']
    assert id == data['id']
    assert text == data['text']
    assert ref == data['ref']
    
@pytest.mark.parametrize('id,text,ref', [
    ('action1', 'An Action', 'https://schema.org/identifier'),
    ('action2', 'Another Action', 'https://schema.org/email')
])
def test_single_safe_descriptor(id, text, ref):
    alps = Alps().add(Safe(id=id, text=text, ref=ref))
    data = alps.to_data()['alps']
    assert 'safe' == data['descriptor']['type']

def test_multiple_descriptors():
    alps = Alps()
    alps.add(Semantic(id='sample1'))
    alps.add(Semantic(id='sample2'))
    alps.add(Safe(id='an_action'))
    data = alps.to_data()['alps']['descriptor']
    assert list == type(data)
    assert 'sample1' == data[0]['id']
    assert 'an_action' == data[2]['id']