# TopoSearch

A federated search service with result aggregation, moderation and feedback mechanism to potentially update the source data. I will try to explain what this means, but first, a brief **disclaimer**:

> *The code and ideas developed in this repository are part of my dissertation. I expect it will be very active until Summary 2022. What will happen next will depend on how useful the output is. If you are interested in similar topics to those used in the project, I'd be [happy to chat](https://www.linkedin.com/in/michalporeba/). If you think my approach makes no sense, I'd love to hear from you - [create an issue](https://github.com/michalporeba/toposearch/issues/new/choose) and let me know where I went wrong.*

Now let me tell you more about the TopoSearch idea…

&nbsp;

# The Problem

We have increasing amounts of data all around us. Discoverability is a challenge. It is especially true in systems where fine-grained access controls are necessary across organisational boundaries.

Public crawling and indexing are not possible. Centralisation of data in data warehouses and lakes is currently the go-to solution. But that means the data governance has to be centralised. While it works in some organisations, it poses significant challenges in heterogeneous systems, and searches across multiple organisations.

The increasing amount of data, gives rise to a growing number of possible search results.

## Why? 

* To improve data discoverability in systems where centralisation of data is not an option
* To improve the search results based on the relative location of the searcher, and the information in the network topology
* To find a mechanism to send feedback and suggest data improvements, from the results, back to the data sources
* To get ready for a more distributed data landscape

## What?

* An API
* A Service
* A Demo (or two)

## How? 
* The search query will be federated (distributed) in a mesh search network
* The results will be filtered by the source systems
* The results will be moderated by the network
* The results will be aggregated before presenting them to the user
* The feedback will be pushed back through the network to the source systems to suggest updates

&nbsp;

# Possible Use Cases

*(A list of possible use cases will have to be developed to better explain the problem and possible applications of the solution)*

&nbsp;

# Technology 

* API: [OpenSearch](https://en.wikipedia.org/wiki/OpenSearch), [OpenAPI](https://swagger.io/specification/), [REST](https://en.wikipedia.org/wiki/Representational_state_transfer), [HAL](https://en.wikipedia.org/wiki/Hypertext_Application_Language), [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS), [JSON-LD](https://json-ld.org/), 
* Back-end: [Python](https://www.python.org/), [Django](https://www.djangoproject.com/)
* Front-end: [JavaScript](https://en.wikipedia.org/wiki/JavaScript), [Design System](https://design-system.service.gov.uk/), [React](https://reactjs.org/)

&nbsp;

## Keywords or topics explored in this project

[Federated Search](https://en.wikipedia.org/wiki/Federated_search), Search Results Aggregation, [OpenSearch](https://en.wikipedia.org/wiki/OpenSearch), Decentralised Data Solutions, Hypermedia in RESTful API, [Hypermedia as the Engine of Application State (HATEOAS)](https://en.wikipedia.org/wiki/HATEOAS)

*TBC*
