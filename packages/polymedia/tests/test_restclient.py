from poly.restclient import RestClient
import responses 

@responses.activate
def test_hello():
    responses.add(responses.GET, 'https://localhost/wstl', json={ 
        'wstl': {
            'title': 'wstl home'
        }}, status=200)
    rc = RestClient()
    poly = rc.hello('https://localhost/wstl')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'https://localhost/wstl'
    assert 'wstl home' == poly.title