# A practical example

Distributed services require more effort to build, but are there any benefits? Let's look at an example of how a Customer Relationship Management (CRM) type service could benefit from distribution, and application of hypermedia in service interactions design. 

## Setting the stage

To explain the benefits, let's look at an example with diagrams. Here are the main symbols I'm going to use. 

![](images/crm-legend.png)

Let's imagine a CRM, a service used to handle information about business, people, events and locations. We wnat to extend its functionality by leveraging a few existing services (A, B, C) through the APIs they provide. The services may provide some infromation about some entities, or offer simple operations, or even provide end user services of their own. 

![](images/crm-s0.png)

## Possible solutions

One way to do it, is be building custom UI elements in the CRM specific to each of the services API. The work has to be repeated for each service and the CRM becomes dependant on the APIs provided by the services it consumes. 

There solution appears reasonable, but if the services provide their own UI there might be some duplication of effort as now two teams must create UI for the same functionality. 

![](images/crm-s0-1.png)

Micro UIs, also knowas micro front-ends is another possibility. The teams building individual service must now provide not only the API, but UI that communicates with that API. There is more effort on the service teams, but they could leverage the same micro UI in their services. The added benefit is, that the same UI can be used in the service, and to provide the same functionality in the CRM providing user familiarity. 

The CRM team must provide a way to host the micro UIs. Not only is that an added effort, but might result in two way dependency. This solution works best in closed organisations where technology can be synchronised. 

A significant downside is that the CRM team loses control over the UI they provide to their user potentially leading to, paradoxically, a more fragmented user experience despite the close integration. 

![](images/crm-s0-2.png)

Hypermedia in API offers yet another approach. In the *ODIS* project I'm exploring the possibility of leveraging those concepts to solve the integration problems. 

Let's assume that ODIS is developed, and working as intended. The CRM has to use the client package provided to extend its functionality, and implement changes to its UI, to be able to respond to some simple, standard ODIS data types. 

The Services, in adition to providing their own UI and API, have to implement (using packages provided) the ODIS endpoints necessary for integration. 

The dependencies of all services, including the CRM are on a small, well defined protocol of ODIS regardless of the specific functionality provided. It might not offer a lot of benefit, but hopefully I will be able to show in below that it actually changes a lot. 

![](images/crm-s0-3.png)

## The interactions

To show how the hypermedia differs from the other two architectures, let's look how the ODIS interaction mechanics look like. 

First, we assume that the ODIS network already exists and works with all the necessary standards defined. For the first part of the example it would be enough for a single ODIS node to exist. 

The services, in their own time and when they are ready register with that node providing standardised description of entities they deal with, operations and services they provide. 

CRM service joins the netwrok too, but without registering any services. (This is not a requirement. It could provide services too, but for simplicity, let's assume it doesn't). Even though the CRM doesn't provide any services, this setup operation is necessary, so the permissions can be configured. 

![](images/crm-s1-1.png)

Now, a user logs in to a CRM and decides to search for a business by name. Since ODIS provides search functionality, the search from the CRM UI is passed to ODIS, and the node federates the search to all registered services which declared at registration that they support the search functionality. To make the search more specific CRM can pass on information about the entity type the user is interested. The services should honour that detail. 

![](images/crm-s1-2.png)

Not all services will have information, but some might and some they return search results. The ODIS network handles the result aggregation, deduplication and responds with an aggregated result set to CRM, where the information is presented to the user in the way fully controlled by the CRM team. 

![](images/crm-s1-3.png)

*This step is optional and makes sense only if the CRM is not only an aggregator of services, but contains its own data on the entities it manages.*

The user now decides to 'open' one of the results provided. While the core of the information is provided by the CRM, it passes on the request for details/highlights/summary of the entity and any operations and services available to all the services in the network. 

The requested information is returned in a hypermedia format, and rendered in a standard way to the user. 

![](images/crm-s1-4.png)

Thanks to the hypermedia, it is now possible to invoke actions through CRM UI in the services that provided the data. But this might be useful only for simply actions, simple enough to be rendered in a standardised way from hypermedia alone. 

![](images/crm-s1-5.png)

What is the service offered by one of the services is more complex and comes with its own complex user interaction? In that case, the interaction should be transfered to that service. 

![](images/crm-s1-6.png)

## Potential benefits

So far it might look like extra work. Why such indirection in using APIs? Not only it requires more work, but necesarily the integration has to be less complex, more generic, perhaps puting limitations on what user experience we can offer. 

The benefits, especially over micro UI approach, become more appraent when we look at what happens when we cross organisational boundaries where standardisation becomes a significant challenge. 

The ODIS network offers a standard way of extending the interactions describe above across the organisational boundaries using a small and well defined API. The hypermedia use in the API reduces the dependencies on specifics of any API design even inside the ODIS network. 

The extension of the network and functionality will require some work around the security and set up of trust in between the participating organisations, but it should be easier than agreeing exchange of bulk data and discussing data ownership. Each organisation remains the owner of data and in full control of the services it provides. The decision whether to provide the service, or disclose the data can be made on each request. 

![](images/crm-s2-1.png)

The added benfit is, that each organisation is free to create their own user interfaces, their own CRMs, or any systems that can freely benefit from the network of services dealing with individual entities. 

In this example the functionality from services D, E and F can be accessed by both users, but each using their prefered application with a familiar UI. 

![](images/crm-s2-2.png)

The most important element is how this network of services can be extended. Should 'another organisation' develop a service G providing some service to do with businesses, locations, people or events, all it has to do is to register the service in the ODIS network, for that functionality to be (potentially immediately) surfaced in the CRM. The CRM user gets more out of the CRM while the Service G team gets more use out of their service improving the transaction cost and the in a federated world, better return on investment. 

![](images/crm-s2-3.png)

## Bringing it all together

While there might be some necessary reduction in detail of what is possible in CRM from the user experience point of view, we gain something else in the same regard. With very little effort on the CRM team (or the user) the functionality, the information the CRM can offer to the user, keeps growing offering user experience benefits. 

![](images/crm-start.png)