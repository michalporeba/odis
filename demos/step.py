from rdflib import Graph, term
from pyld import jsonld

g = Graph()
g.parse("data/exporters.json")
g.parse("data/importers.json")
g.parse("data/companies.json")
print(g.serialize(format="turtle"))

print('------')

framed = jsonld.frame({
    "@graph": {
        "https://schema.org/name": "Dewi"
    }
}, {
         '@id': 'https://exmaple.com/1',
         '@context': {
             '@vocab': 'http://www.bbc.co.uk/ontologies/webmodules/',
             'hello': 'helo'
         },
         "contains": {
             "a": "1"
         },
         '@type': 'WebModule',
         'type': 'hello',
         'importer': 'imp',
         'i': 'importer'
     })


print('====')
for (_,value) in g[:term.URIRef('https://schema.org/name')]:
    print(value)
print('+++++')
qres = g.query("""
select ?name ?number
where {
    ?s <https://schema.org/name> ?name .
    optional {
        ?s <https://schema.gov.uk/companynumber> ?number
    }
}
""")

for row in qres:
    number = getattr(row, 'number', 'UNKNOWN')
    print(f'{row.name} ({number})')
