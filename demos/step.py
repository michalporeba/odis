from rdflib import Graph, term, OWL
from pyld import jsonld

g = Graph()
g.parse("data/exporters.json")
g.parse("data/importers.json")
g.parse("data/companies.json")
g.add((term.URIRef('https://schema.gov.uk/companynumber'), OWL.sameAs, term.URIRef('https://companieshouse.gov.uk/schema/companynumber')))
g.add((term.URIRef('https://schema.gov.uk/companynumber'), OWL.sameAs, term.URIRef('https://schema.gov.uk/companynumber')))
print(g.serialize(format="turtle"))




print('====')
for (_,value) in g[:term.URIRef('https://schema.org/name')]:
    print(value)

frame = jsonld.frame(g, {})

print('+++++')
qres = g.query("""
select ?name ?number
where {
    ?s <https://schema.org/name> ?name .
    optional {
        <https://schema.gov.uk/companynumber> owl:sameAs ?cna .
        ?s ?cna ?number
    } .
    optional { 
        ?a <https://dit.schema.gov.uk/numberOfExports> ?exports .
    }
}
""")

for row in qres:
    print(row.labels)
    number = getattr(row, 'number', 'UNKNOWN')
    exports = getattr(row, 'exports', '0')
    print(f'{row.name} ({number}), Exports = {exports}')
