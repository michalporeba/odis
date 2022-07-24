from sam import *
from rdflib import Graph, term, OWL

term_name = term.URIRef('http://schema.org/name')

g = Graph()
addSameAs(g)

g.parse(connect_to_companies_service())

g.update('''
    insert { ?company <http://schema.gov.uk/primaryName> ?name }
    where { ?company <http://schema.org/name> ?name }
''')

g.parse(connect_to_exporters_service())
g.parse(connect_to_importers_service())

results = g.query('''
    select ?name ?number ?imports ?exports
    where { 
        ?company <http://schema.gov.uk/primaryName> ?name .
        optional {
            <http://schema.gov.uk/companyNumber> owl:sameAs ?cna .
            ?company ?cna ?number
        } .
        optional {
            ?company <http://schema.gov.uk/dit/numberOfImportedProducts> ?imports
        } .
        optional {
            ?company <http://schema.gov.uk/dit/numberOfExportedProducts> ?exports
        }
    }
''')

for r in results:
    imports = r.get('imports', 0)
    exports = r.get('exports', 0)
    number = r.get('number', 'UNKNWON')
    print(f'{r.name} ({number}) Imports: {imports} Exports: {exports}')