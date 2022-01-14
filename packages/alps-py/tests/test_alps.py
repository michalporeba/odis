import pytest
import json
from alps import *
from alps.schemaorg import SchemaOrg
from diogi.conventions import to_data

def test_root_is_alps():
    root = to_data(Alps())
    assert 1 == len(root.keys())
    assert None != root['alps']

def test_version_defaults_to_one():
    data = to_data(Alps())['alps']
    assert '1.0' == data['version']

@pytest.mark.parametrize('attribute', ['title', 'doc', 'descriptor'])
def test_there_are_no_unnecessary_attributes_by_default(attribute: str):
    data = to_data(Alps())['alps']
    assert attribute not in data.keys()

@pytest.mark.parametrize('alps_title', ['Sample API', 'Another API'])
def test_title_from_constructor(alps_title: str):
    alps = Alps()
    alps.set_title(alps_title)
    data = to_data(alps)['alps']
    assert alps_title == data['title']

@pytest.mark.parametrize('text', ['abc', 'def'])
def test_markdown_documentation(text: str):
    alps = Alps().add_doc(MarkDownDoc(text))
    data = to_data(alps)['alps']
    assert 'markdown' == data['doc']['format']
    assert text == data['doc']['value']

@pytest.mark.parametrize('id,text,ref', [
    ('identifier', 'Unique Identifier', 'https://schema.org/identifier'),
    ('email', 'Test email address', 'https://schema.org/email')
])
def test_single_semantic_descriptor(id, text, ref):
    alps = Alps()
    alps.add_descriptor(Semantic(id=id, text=text, ref=ref))
    data = to_data(alps)['alps']['descriptor']
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
    alps = Alps().add_descriptor(Safe(id=id, text=text, ref=ref))
    data = to_data(alps)['alps']
    assert 'safe' == data['descriptor']['type']

def test_multiple_descriptors():
    alps = Alps()
    alps.add_descriptor(Semantic(id='sample1'))
    alps.add_descriptor(Semantic(id='sample2'))
    alps.add_descriptor(Safe(id='an_action'))
    data = to_data(alps)['alps']['descriptor']
    assert list == type(data)
    assert 'sample1' == data[0]['id']
    assert 'an_action' == data[2]['id']

def test_nested_descriptor_with_docs():
    alps = Alps()
    desc = SchemaOrg.IDENTIFIER
    desc.add_doc(MarkDownDoc('test documentation'))
    alps.add_descriptor(desc)
    data = to_data(alps)['alps']['descriptor']
    assert 'test documentation' == data['doc']['value']

def test_alps_can_parse_an_empty_or_invalid_dictionary(caplog):
    with open(f'tests/data/empty.json') as f:
        data = json.load(f)

    alps = Alps.parse(data)
    assert Alps == type(alps)
    assert None == alps.title
    assert None == alps.version
    assert 'does not contain ALPS' in caplog.text

@pytest.mark.parametrize("data", [None, ''])   
def test_alps_does_not_chocke_on_invalid_input(data, caplog):
    alps = Alps.parse(None)
    assert Alps == type(alps)
    assert None == alps.title
    assert None == alps.version
    assert 'does not contain ALPS' in caplog.text


def test_alps_json_parsing_on_sample_1():
    with open(f'tests/data/sample1.json') as f:
        data = json.load(f)

    #alps = Alps.parse(data)