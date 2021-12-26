# Architecture

This document is part of the [architecture](./architecture.md) topic. 

## Container view

![Container](./images/c4-container.png)

In the container view, we can look closer at the elements of the TopoSearch Network. 

* **Search Node** - the service providing the API and the basic UI to build and operate the search network. It does the query federation, response moderation and aggregation. 
* **Standard Connector** - a plugin facilitating search services that implement the standard protocol. 
* **3rd Party Connector** - plugins facilitating search in services that do not implement the standard protocol. For example, search in SharePoint or in ElasticSearch.
* **Audit Producer** - a plugin that saves the data or delivers audit data for SEIM systems. 

---
## Read More 
* [Context View](./a-context-view.md)