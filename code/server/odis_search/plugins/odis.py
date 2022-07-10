import requests 

def search_in_odis_node(url: str, query: str) -> list:
    headers = {
        'Accept': f'application/json'
    }

    response = requests.get('http://127.0.0.1:8081/odis/search', headers=headers, params = { 'q': query })
    return [] 
    response.json()