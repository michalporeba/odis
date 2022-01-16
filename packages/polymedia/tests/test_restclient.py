from alps import Alps, Descriptor
from polymedia.restclient import RestClient
from polymedia.wstl import Wstl 
from responses import matchers
import responses 
import json 

JSON_BLANK_PATH = 'json/blank'
JSON_BLANK_URL = 'https://localhost.tests/json/blank'
JSON_WSTL_PATH = 'json/wstl-like'
JSON_WSTL_URL = 'https://localhost.tests/json/wstl-like'
WSTL_HELLO_PATH = 'wstl/hello'
WSTL_HELLO_URL = 'https://localhost.tests/wstl/hello'
WSTL_TEST_PATH = 'wstl/test'
WSTL_TEST_URL = 'https://localhost.tests/wstl/test'
NONE_WSTL_PATH = 'none/wstl'
NONE_WSTL_URL = 'https://localhost.tests/none/wstl'


def add_response(method, path: str, params: dict | None = None, body: dict = None):
    with open(f'tests/responses/{path}.json') as f:
        data = json.load(f)

    accepted_type = 'application/json'
    if 'wstl/' in path:
        accepted_type = Wstl.MIME_TYPE 
    if 'alps' in path:
        accepted_type = 'application/alps+json'
    if 'none/' in path: 
        accepted_type = None

    responses.add(
        method,
        f'https://localhost.tests/{path}',
        json=data,
        status=200,
        headers=None if accepted_type is None else {'Content-Type': accepted_type},
        match=[] if body is None else [matchers.json_params_matcher(body)] +
            [] if params is None else [matchers.query_param_matcher(params)]
    )


def add_get_response(path: str, params: dict | None = None):
    add_response(responses.GET, path, params)


def setup_alps_tests():
    add_get_response('alps/sample1')
    add_get_response('wstl/alps-one')
    add_get_response('wstl/get-with-alps', params={'q': 'value-of-q'})
    add_get_response('wstl/get-without-alps')
    add_get_response('wstl/test-with-alps')
    add_response(responses.POST, 'wstl/post-one', body={'size': 123})
    add_response(responses.POST, 'wstl/post-two', body={'width': 12, 'height': 34})
    rc = RestClient()
    rc.connect('https://localhost.tests/wstl/test-with-alps')
    return rc


@responses.activate
def test_first_get():
    add_get_response(WSTL_HELLO_PATH)
    rc = RestClient()
    poly = rc.connect(WSTL_HELLO_URL)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == WSTL_HELLO_URL
    
    assert Wstl == rc.formatter
    assert 'wstl home' == poly.title


@responses.activate 
def test_get_negotiates_content_with_json_fallback():
    add_get_response(WSTL_HELLO_PATH)
    rc = RestClient()
    poly = rc.connect(WSTL_HELLO_URL)

    headers = responses.calls[0].request.headers
    assert 'wstl' == rc.format
    assert 4 == len(headers)
    assert 'application/vnd.hal+json' in headers['Accept']
    assert 'application/prs.wstl+json' in headers['Accept']
    assert 'application/json' in headers['Accept']


@responses.activate
def test_get_does_not_break_if_json_response():
    add_get_response(JSON_BLANK_PATH)
    rc = RestClient()
    poly = rc.connect(JSON_BLANK_URL)

    assert None == rc.formatter


@responses.activate
def test_perform_action():
    add_get_response(WSTL_HELLO_PATH)
    add_get_response(WSTL_TEST_PATH)
    rc = RestClient()

    poly = rc.connect(WSTL_HELLO_URL)
    assert 'wstl home' == poly.title

    poly = rc.do('test')
    assert 'wstl test' == poly.title
    assert 'testing wstl' == poly.data[0]['test']


@responses.activate
def test_action_checks():
    add_get_response(WSTL_HELLO_PATH)
    rc = RestClient()
    rc.connect(WSTL_HELLO_URL)

    assert True == rc.can_do('self')
    assert True == rc.can_do('home')
    assert True == rc.can_do('test')
    assert False == rc.can_do('missing')


@responses.activate 
def test_actions_list():
    add_get_response(WSTL_HELLO_PATH)
    rc = RestClient()
    rc.connect(WSTL_HELLO_URL)

    assert 'self' in rc.actions
    assert 'home' in rc.actions
    assert 'test' in rc.actions


@responses.activate
def test_wstl_should_work_even_if_mime_time_is_json():
    add_get_response(JSON_WSTL_PATH)
    rc = RestClient()
    rc.connect(JSON_WSTL_URL)

    assert Wstl == rc.formatter
    assert 'wstl' == rc.format
    assert 'jason with wstl structure' == rc.poly.title
    assert True == rc.can_do('self')
    assert True == rc.can_do('home')
    

@responses.activate
def test_action_dropping_accept_header():
    add_get_response(WSTL_HELLO_PATH)
    add_get_response(WSTL_TEST_PATH)
    add_get_response(NONE_WSTL_PATH)
    rc = RestClient()
    rc.connect(WSTL_HELLO_URL)
    rc.do('test')
    poly = rc.do('none')

    assert 'wstl with no header' == poly.title
    poly = rc.do('home')
    assert 'wstl home' == poly.title


@responses.activate
def test_automatic_alps_from_wstl():
    def noop_resolver():
        # important to test behaviour when alps exists and 
        # can be used - because there is a resolver
        # without it an error mode cannot be tested
        pass 

    rc = setup_alps_tests()
    assert Alps == type(rc.alps)
    assert 'part of WSTL' in rc.alps.title 

    # ensure actions not defined in ALPS can be still performed
    poly = rc.do('get-without-alps', noop_resolver)
    assert 'value from get-without-alps' == poly.data[0]


@responses.activate 
def test_wstl_get_parameters_using_alps():
    rc = setup_alps_tests()

    def value_resolver(descriptor: Descriptor) -> any: 
        if descriptor.id == 'q':
            return 'value-of-q'
        elif descriptor.id == 'size':
            return 123
        elif descriptor.id == 'width':
            return 12
        elif descriptor.id == 'height':
            return 34
        else: 
            return 'something else'

    poly = rc.do('get-with-alps', value_resolver)
    assert 'value from get-with-alps' == poly.data[0]
    rc.do('home')
    # to succeed it will have to automatically resolve size
    poly = rc.do('doPostOne', value_resolver)
    assert 'response to post one' == poly.data[0]
    rc.do('home')
    # to succeed it will have to resolve width and height
    poly = rc.do('doPostTwo', value_resolver)
    assert 'response to post two' == poly.data[0]
