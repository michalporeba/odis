# Demo notes

## The exporters service

DIT creates an exporters service. Data is in JSON and can be easily read. 

```python
import json 

exporters = json.load(open('data/exporters.json'))['exporters']
print(exporters)
```

Let's format the output into a list of names

```python
import json 

exporters = json.load(open('data/exporters.json'))['exporters']

for exporter in exporters:
    print(exporter['name'])
```

Print both, and then try to combine the list to get all the companies and types

```python
import json 

exporters = json.load(open('data/exporters.json'))['exporters']
importers = json.load(open('data/importers.json'))['importers']

exporter_names = [e['name'] for e in exporters]
importer_names = [i['importer'] for i in importers]

companies = [name for name in set(exporter_names + importer_names)]

for company in companies:
    print(company)
```

Using linked data
```python
from rdflib import Graph, term
from pyld import jsonld

g = Graph()
g.parse("data/exporters.json")
g.parse("data/importers.json")

for (_,value) in g[:term.URIRef('https://schema.org/name')]:
    print(value)
```

Query
```python
qres = g.query("""
select ?name
where {
    ?s <https://schema.org/name> ?name 
}
""")

for row in qres:
    print(row.name)

```


```python
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
```

And with alternative name by companies house

```python
qres = g.query("""
select ?name ?number
where {
    ?s <https://schema.org/name> ?name .
    optional {
        ?s (<https://schema.gov.uk/companynumber>|<https://companieshouse.gov.uk/scheme/companynumber>) ?number
    }
}
""")
```


```python
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
```

# notes
An example of company URI from CH Basic Data

http://business.data.gov.uk/id/company/10013084




