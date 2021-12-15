# Product Overview from Search (Use Case 2)

Information in organisations is often stored in multiple services, 
especially when ystems are implemented as a group of microservices. 
The example could be about any entity stored in multiple systems, for example:
* **Employees** in Human Resources systems
* **Business** in Enterprise Resource Planning (ERP) systems
* **Products** in retail, manufacturing, ERP 

While examples would be very similar, but to avoid any sensitive information 
and stay with mostl widely understandable problems, this use case is about Products. 

## Background 

Imagine a company that manufactures toys and sells them either to retailers
or to individual (online). Their system consists of multiple microservices: 
* **Inventory** - How many of what do we have?
* **Manufacturing** - Taking parts and making the whole, including production schedules. 
* **Sales** - Bulk, business to business sales records including longer term orders. 
* **Shop** - Individual, retail sales including presentation and description
* **Shipment** - Deliveries to both bulk and individual purchases.

## TopoSearch in the mix

Currently, the only way to build a broader understading of a product, 
is to look at all of the services. A standard solution would be 
to create a data warehouse, where all the data comes together.

TopoSearch approach could offer an alternative solution, in this
simple scenario with a singe node.

### Search Federation

The search for a product gets submitted to the search node
which federates the request to all five services. 

### Result Aggregation 

All services could return multiple results. For example:
* **Inventory** service could return a record representing quantity of the product in each warehouse or storage location. 
* **Manufacturing** service could return the list of scheduled builds, or a list of materials needed to create the product.
* **Sales** service could show all the orders, or only those upcoming, or other products typically bought together. 
* **Shop** service could return similar data to those from *Sales* but relating to individuals rather than companies.
* **Shipment** service could return list of shipments including the product, perhaps with state, delivery date and distance. 

Because we are dealing with searching for a specific entity rather
than performing a lexical search on unstructured data, 
we don't have to overwhelm the user with all possible search results. 
Instead, we can present an aggregated view of a product. 
We could show a 'tile' for each type of information with a brief
summary, and ability to drill into the details. 

### Feedback

* **Manfuacturing** service could expose an action to request 
an increase or decrease in production. So after searching, and seeing
the bigger picture it would be easy to take action. 
* **Sales** and **Shop** could both expose an action to request
the product to be taken off the sales list.

Of course, things like that would be possible without the feedback, but the feedback mechanism could allow for more integrated user experience, and ability to show that a request has been made on the next search, even before it has been processed. 

## The extra mile

The use case so far can be facilitated with a single search node in the organisation. But it could be extended. 

### Extending the Network

The search network could be extended to business customers and suppliers. The customers could search for products through the unified search interface, while suppliers of parts could allow for their products to be search through the network. 

If the suppliers were to include their current prices in the search results, and our services included our costs and prices, we could include margin calculation directly in the search results.

### Result Moderation

But to make this cross-organisation collaboration possible, the search results would have to be moderated before exposing them outside of the organisation which controls the data. 

The same service could expose varying degree of data depedning on who is asking for information, of course, but that would mean implementing the logic in each service. Instead the search service could implement data moderation feature, to control what information is passed upstream in response to a search request. 