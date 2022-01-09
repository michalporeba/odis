# Product Overview from Search (Use Case 2)

Organisations' information is often stored in multiple services, especially 
when systems are implemented as a group of microservices. The example could be 
about any entity stored in multiple systems, for example:

* **Employees** in Human Resources systems
* **Business** in Enterprise Resource Planning (ERP) systems
* **Products** in retail, manufacturing, ERP 

While the example variations would be very similar to avoid any sensitive 
information and stay with the most widely understandable problems, this use case
is about *Products*. 

## Background 

Imagine a company that manufactures toys and sells them either to retailers
or individuals (online). Their system consists of multiple microservices:

* **Inventory** - How many of what do we have?
* **Manufacturing** - Taking parts and making the whole, including production schedules. 
* **Sales** - Bulk, business to business sales records, including longer-term orders. 
* **Shop** - Individual, retail sales including presentation and description
* **Shipment** - Deliveries to both bulk and individual purchases.

## ODIS in the mix

The only way to build a broader understanding of a product is to look at 
all services. A standard solution would be to create a data warehouse where 
all the data comes together.

Open Distributed Information Sharing approach could offer an alternative solution in this simple 
scenario with a single node.

### Search Federation

The search for a product gets submitted to the search node,
which federates the request to all five services. 

### Result Aggregation 

All services could return multiple results. For example:
* **Inventory** service could return a record representing the quantity of the product in each warehouse or storage location.
* **Manufacturing** service could return the list of scheduled builds, or materials needed to create the product.
* **Sales** service could show all the orders, or only those upcoming or other products typically bought together. 
* **Shop** service could return similar data to *Sales* but relating to individuals rather than companies.
* **Shipment** service could return alist of shipments including the product, perhaps with state, delivery date and distance. 

Because we are dealing with searching for a specific entity rather
than performing a lexical search on unstructured data. We don't have to overwhelm 
the user with all possible search results. Instead, we can present an aggregated
view of a product. For example, we could show a 'tile' for each type of information
with a brief summary and the ability to drill into the details.

### Feedback

* **Manufacturing** service could expose an action to request 
an increase or decrease in production. So after searching and seeing
the bigger picture, it would be easy to take action. 
* **Sales** and **Shop** could both expose an action to request
the product to be taken off the sales list.

Of course, things like that would be possible without the feedback. Still,
the feedback mechanism could allow for a more integrated user experience
and the ability to show that a request has been made on the following search,
even before it has been processed.

## The extra mile

The use case can be facilitated with a single search node in the organisation.
But it could be extended.

### Extending the Network

The search network could be extended to business customers and suppliers.
The customers could search for products through the unified search interface,
while suppliers of parts could allow their products to be explored through the network.

If the suppliers included their current prices in the search results and our
services included our costs and prices, we could include margin calculation
directly in the search results.

### Result Moderation

But to make this cross-organisation collaboration possible, the search results
would have to be moderated before exposing them outside of the organisation
which controls the data.

The same service could expose the varying degree of data depending on who
is asking for information, of course, but that would mean implementing
the logic in each service. So instead, the search service could implement
a data moderation feature to control what information is passed upstream
in response to a search request.