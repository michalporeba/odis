from rdflib import Graph
from pyld import jsonld

g = Graph()
g.parse("data/exporters.json")
g.parse("data/importers.json")
print(g.serialize(format="turtle"))

query = """
select ?name ?type
where {
    ?org rdf:type ?type
}
"""

qres = g.query(query)

for row in qres:
    print(f"{row.name} is an {row.type}")

print('------')

jld = g.serialize(format="json-ld")
print(jld)

framed = jsonld.frame(g, { 
    "type": "array",
    "items": { "name": "https://schema.org/name" }
})

framed = jsonld.frame(g, {
         '@context': {
             '@vocab': 'http://www.bbc.co.uk/ontologies/webmodules/'
         },
         '@type': 'WebModule'
     })
print(framed)
print(g.toPython())