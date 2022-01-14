from multiprocessing.sharedctypes import Value
import pytest
from alps.docs import *

def assert_is_text_doc(doc: Doc):
    assert TextDoc == type(doc)
    assert 'text' == doc.format
    assert None == doc.href
    assert None == doc.tag 
    

def test_none_parses_to_empty_text_doc():
    doc = Doc.parse(None)
    assert_is_text_doc(doc)
    assert '' == doc.value
    

def test_string_parses_to_text_doc():
    doc = Doc.parse('hello')
    assert_is_text_doc(doc)
    assert 'hello' == doc.value


def test_odd_object_parses_to_text_doc():
    doc = Doc.parse({ 'a': 2})
    assert_is_text_doc(doc)
    assert "{'a': 2}" == doc.value


def test_no_format_with_value_parses_to_text_doc():
    doc = Doc.parse({ 'value': 'first'})
    assert_is_text_doc(doc)
    assert 'first' == doc.value


def test_unsupported_format_parses_to_text_doc():
    doc = Doc.parse({ 'format': 'not-supported', 'value': 'second'})
    assert_is_text_doc(doc)
    assert 'second' == doc.value


def test_markdown_parsed_to_markdown():
    doc = Doc.parse({ 'format': 'markdown', 'value': 'hello **MarkDown**'})
    assert MarkDownDoc == type(doc)
    assert 'markdown' == doc.format 
    assert None == doc.href
    assert 'hello **MarkDown**' == doc.value

def test_html_parsed_to_html():
    doc = Doc.parse({ 
        'format': 'html', 
        'href': 'test://url.com',
        'value': '<h1>hello</h1>'
    })
    assert HtmlDoc == type(doc)
    assert 'html' == doc.format
    assert '<h1>hello</h1>' == doc.value
    assert 'test://url.com' == doc.href