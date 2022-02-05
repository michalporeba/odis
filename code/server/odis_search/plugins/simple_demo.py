import requests 
import uuid 


def search_in_simple_demo(url: str, query: str) -> list:
    headers = {
        'Accept': f'application/json'
    }

    response = requests.get(url, headers=headers, params = { 'q': query })
    return response.json()
    