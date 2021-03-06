from rdflib import Graph, term, OWL
from pyld import jsonld

g = Graph()
g.parse("data/exporters.json")
g.parse("data/importers.json")
g.parse("data/companies.json")
g.add((term.URIRef('https://schema.gov.uk/companynumber'), OWL.sameAs, term.URIRef('https://companieshouse.gov.uk/schema/companynumber')))
g.add((term.URIRef('https://schema.gov.uk/companynumber'), OWL.sameAs, term.URIRef('https://schema.gov.uk/companynumber')))
#print(g.serialize(format="turtle"))




print('====')
for (_,value) in g[:term.URIRef('https://schema.org/name')]:
    print(value)


print('+++++')
qres = g.query("""
select ?name ?number
where {
    ?s <https://schema.org/name> ?name .
    optional {
        <https://schema.gov.uk/companynumber> owl:sameAs ?cna .
        ?s ?cna ?number
    }
}
""")

for row in qres:
    number = getattr(row, 'number', 'UNKNOWN')
    print(f'{row.name} ({number})')
