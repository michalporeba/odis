from sam import *
from pprint import pprint as pp


def standard_company(company):
    return {
        'name': company['CompanyName'],
        'number': company['CompanyNumber']
    }


def standard_exporter(exporter):
    return {
        'name': exporter['name'],
        'exports': exporter['exportedProducts']
    }


def standard_importer(importer):
    return {
        'name': importer['importer'],
        'imports': importer['importedProducts']
    }


companies = get_data_from_the_companies_service()
companies = [standard_company(c) for c in companies]

exporters = get_data_from_the_exporters_service()
exporters = [standard_exporter(e) for e in exporters]

importers = get_data_from_the_importers_service()
importers = [standard_importer(i) for i in importers]

results = {}
alternatives = {
    'Pinafal': 'Pinafal Ltd',
    'Pinafal LTD': 'Pinafal Ltd',
    'Pwmpen.co.uk': 'Pwmpen',
    'Melon': 'Melon and Co.'
}

for c in exporters+importers:
    name = alternatives.get(c['name'], c['name'])
    if name not in results:
        results[name] = c
    else:
        results[name] |= c
    results[name]['name'] = name

for c in companies: 
    name = alternatives.get(c['name'], c['name'])
    if name in results:
        results[name]['number'] = c.get('number', 'UNKNOWN')

results = list(results.values())

pp(results)