from rdflib import Graph, term
from pyld import jsonld

g = Graph()
g.parse("data/exporters.json")
g.parse("data/importers.json")
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

print(framed)
print(g.commit())
print('====')
for (_,value) in g[:term.URIRef('https://schema.org/name')]:
    print(value)
print('+++++')
qres = g.query("""
select ?name
where {
    ?s <https://schema.org/name> ?name 
}
""")

for row in qres:
    print(row.name)
