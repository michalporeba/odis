from pyld import jsonld
import json

#compacted = jsonld.compact('http://demo.gov.uk/companies.json', 'http://schema.gov.uk/company.jsonld')
expanded = jsonld.expand('http://demo.gov.uk/companies.json')

print(json.dumps(expanded, indent=2))