from rdflib import Graph, term
from pyld import jsonld
from departaments.sam import * 

g = Graph()
g.parse(connect_to_companies_service2())

g.update("""
    insert { ?company <http://schema.gov.uk/dit/primaryName> ?name}
    where { ?company <http://schema.org/name> ?name }
""")

g.parse(connect_to_exporters_service2())
g.parse(connect_to_importers_service2())

frame = jsonld.frame(g, {
    "@context": {
        "@version": 1.1
    },
    "@type": "http://schema.gov.uk/company",
    "contains": {
        "@type": "Book",
        "contains": {
            "@type": "Chapter"
        }
  }
})

print(frame)
