# Architecture

The architecture presented here, at least at the moment, is not meant
to be a blueprint for the implementation of the solution, but rather
a tool to help me - and others - to understand the problems the project
attempts to solve and the constraints within which the solution has to operate. 

To capture the architecture I use the [C4 modelling notation](https://c4model.com/) and [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language).

## Proposed Solution Overview

* [Context View (C4)](./a-context-view.md)
* [Container View (C4)](./a-container-view.md)
* [Use Cases (UML)](./a-use-cases.md)

## Other Things to Consider

* [Interactions Map (In Progress)](./interactions.md)

### Software Development Kit (SDK)

The SDK is outside of the TopoSearch Network system. It is intended to be used by service developers to help with the rapid development of endpoint implementing the agreed search protocol. 

### Future improvements

While the Search Node provides all the necessary UI, reacher clients could be created for a better user experience. 

* **Admin Client** - an application for management of the search network.
* **Search Client** - an application for searching across the network.

## Protocols inside and outside of the network

![Protocols](./images/c4-protocols.png)
