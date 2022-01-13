from poly.restclient import RestClient
from poly.wstl import Wstl 
import responses 
import json 

JSON_BLANK_PATH = 'json/blank'
JSON_BLANK_URL = 'https://localhost.tests/json/blank'
WSTL_HELLO_PATH = 'wstl/hello'
WSTL_HELLO_URL = 'https://localhost.tests/wstl/hello'

def add_get_response(path: str): 
    with open(f'tests/responses/{path}.json') as f:
        data = json.load(f)

    accepted_type = 'application/json'
    if 'wstl/' in path:
        accepted_type = Wstl.MIME_TYPE 

    responses.add(
        responses.GET, 
        f'https://localhost.tests/{path}', 
        json=data, 
        status=200,
        headers={'Accept': accepted_type}
    )

@responses.activate
def test_hello():
    add_get_response(WSTL_HELLO_PATH)

    rc = RestClient()
    poly = rc.hello(WSTL_HELLO_URL)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == WSTL_HELLO_URL
    
    assert Wstl == rc.formatter
    assert 'wstl home' == poly.title

@responses.activate 
def test_hello_negotiates_content_with_json_fallback():
    add_get_response(WSTL_HELLO_PATH)

    rc = RestClient()
    poly = rc.hello(WSTL_HELLO_URL)

    headers = responses.calls[0].request.headers
    assert 4 == len(headers)
    assert 'application/vnd.hal+json' in headers['Accept']
    assert 'application/prs.wstl+json' in headers['Accept']
    assert 'application/json' in headers['Accept']

@responses.activate
def test_hello_does_not_break_if_json_response():
    add_get_response(JSON_BLANK_PATH)

    rc = RestClient()
    poly = rc.hello(JSON_BLANK_URL)

    assert None == rc.formatter