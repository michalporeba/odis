import json
from rdflib import term, OWL

def get_data_from_the_exporters_service():
    return json.load(open('data/exporters.json'))

def get_data_from_the_importers_service():
    return json.load(open('data/importers.json'))

def get_data_from_the_companies_service():
    return json.load(open('data/companies.json'))

def connect_to_exporters_service():
    return 'data/exporters.json'

def connect_to_importers_service():
    return 'data/importers.json'

def connect_to_companies_service():
    return 'data/companies.json'

def connect_to_companies_service2():
    return 'departaments/data/companies.json'

def connect_to_exporters_service2():
    return 'departaments/data/exporters.json'

def connect_to_importers_service2():
    return 'departaments/data/importers.json'

def add_same_as(g):
    g.add(
        (term.URIRef('http://schema.gov.uk/companyNumber'), 
        OWL.sameAs, 
        term.URIRef('http://schema.gov.uk/companyNumber')))
    g.add(
        (term.URIRef('http://schema.gov.uk/companyNumber'), 
        OWL.sameAs, 
        term.URIRef('http://schema.gov.uk/ch/officialCompanyNumber')))
        

if __name__ == '__main__':
    print('Companies')
    print(get_data_from_the_companies_service())
    print('Exporters:')
    print(get_data_from_the_exporters_service())
    print('Importers:')
    print(get_data_from_the_importers_service())