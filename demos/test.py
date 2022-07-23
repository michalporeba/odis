from rdflib import Graph, term, OWL
from pyld import jsonld

g = Graph()
g.parse("http://demo.gov.uk/exporters.json")