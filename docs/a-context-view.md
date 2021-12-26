# Architecture

This document is part of the [architecture](./architecture.md) topic. 

## Context view

![Context](./images/c4-context.png)

At the centre of the solution, there is **the search network**. It consists of several search service instances, typically deployed independently by the organisational units that want to provide search functionality to organisations or people they interact with. 

The search network interacts with four **types of system**:

* **Identity Providers** - the identity is essential in the search network and the source system. However, it is not the responsibility of the search network to act as an identity provider. 
* **Data Service** - any service developed by the organisation which can be closely integrated with the search infrastructure.
* **3rd Party Data Service** - any service storing data which we cannot modify to integrate closely with the search infrastructure.
* **Security Information and Event Management (SIEM)** - systems used in cyber security to look for threats.


There are five **types of users** interacting with the system:

* The **Searcher** - a person looking for information which is at the same time the person who understands the information and can offer feedback.
* The **Data Service Developer** - person who wants to make the information discoverable. 
* The **Search Administrator** - a person responsible for the operation of the search network.
* The **Information Asset Owner / Manager** - person responsible for the information stored in the source service and who is responsible for controlling the access to it. 
* The **Cyber Security Person** - person responsible for maintaining the solution's security. 

---
## Read More 
* [Container View](./a-container-view.md)