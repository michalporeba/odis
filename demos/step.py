import json 

exporters = json.load(open('data/exporters.json'))['exporters']
importers = json.load(open('data/importers.json'))['importers']

exporter_names = [e['name'] for e in exporters]
importer_names = [i['importer'] for i in importers]

companies = [name for name in set(exporter_names + importer_names)]

for company in companies:
    print(company)
