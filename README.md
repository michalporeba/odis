# Open Distributed Information Sharing System (ODIS)

A federated search service with result aggregation, moderation and feedback mechanism to potentially update the source data. 

If you are interested in similar topics to those used in the project, I'd be [happy to chat](https://www.linkedin.com/in/michalporeba/). If you think my approach makes no sense, I'd love to hear from you - [create an issue](https://github.com/michalporeba/odis/issues/new/choose) and let me know where I went wrong.*

Now let me tell you more about the ODIS idea…

&nbsp;

# The Problem

A much fuller description of the problem that motivated the project is available in the [Search for a Better Search](./docs/A%20Search%20for%20a%20Better%20Search.pdfs) paper, but in short...

We have increasing amounts of data all around us. Discoverability is a challenge. It is especially true in systems where fine-grained access controls are necessary across organisational boundaries.

Public crawling and indexing are not possible. Centralisation of data in data warehouses and lakes is currently the go-to solution. But that means the data governance has to be centralised. While it works in some organisations, it poses significant challenges in heterogeneous systems, and searches across multiple organisations.

The increasing amount of data, gives rise to a growing number of possible search results.

## Why? 

* To improve data discoverability in systems where centralisation of data is not an option
* To improve the search results based on the relative location of the searcher, and the information in the network topology
* To find a mechanism to send feedback and suggest data improvements, from the results, back to the data sources
* To get ready for a more distributed data landscape

## What?

**So far there is:**
* [Sample Data Service](./code/sample/) - to provide test and demo data for the project using a range of formats. 
* [Data Exchange Network Node](./code/server/) - The server that can act as a node in the network doing all the federation of requests. 

*Later there will be:*

* A 'Standard' that allows for easy searches in data accross a distributed network of services in a range of [interactions](./docs/interactions.md).
* A Demo (or two)

## How? 
* The search query will be federated (distributed) in a mesh search network
* The results will be filtered by the source systems
* The results will be moderated by the network
* The results will be aggregated before presenting them to the user
* The feedback will be pushed back through the network to the source systems to suggest updates

&nbsp;

# Possible Use Cases

* [Find Me Button](./docs/usecases/findme.md) - Search for and update your personal infromation held by any department accross the Civil Service. 
* [Product Search](./docs/usecases/product-overview.md) - Building the 'bigger picture' of a product through single search without the data warehouse. 
* [Acronym Buster](./docs/usecases/acronyms.md) - An oversimplified example of why topology as context can help improve search results. 
* [No Need for Catalogs](./docs/usecases/nomorecatalogues.md) - Not really a concrete use case, but an sidea what could be possible with federated search approach in terms of data management and governance. 

While I hope the use cases are of use, another way to look at what the search (or data exchange) network can offer, is to look at [possible interactions](./docs/interactions.md) within the system. 

But the distributed systems can do more than just facilitate a search. [The CRM example](./docs/crm.md) illustrated how hypermedia approach to API design can help in building extensible distributed systems. 

&nbsp;

# Architecture

At the moment the project is in a conceptual design stage. 
Have a look at the [solution's architecutre](./docs/architecture.md) as it is developed.

&nbsp;


# Technology 

* API: [OpenSearch](https://en.wikipedia.org/wiki/OpenSearch), [OpenAPI](https://swagger.io/specification/), [REST](https://en.wikipedia.org/wiki/Representational_state_transfer), [HAL](https://en.wikipedia.org/wiki/Hypertext_Application_Language), [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS), [JSON-LD](https://json-ld.org/), 
* Security: [OAuth2.0](https://oauth.net/2/), [Open ID Connect (OIDC)](https://openid.net/connect/), [Json Web Tokens (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token)
* Back-end: [Python](https://www.python.org/), [Django](https://www.djangoproject.com/)
* Front-end: [JavaScript](https://en.wikipedia.org/wiki/JavaScript), [Design System](https://design-system.service.gov.uk/), [React](https://reactjs.org/)

