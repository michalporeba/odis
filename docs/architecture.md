# Architecture

The architecture presented here, at least at the moment, is not meant
to be a blueprint for the implementation of the solution, but rather
a tool to help me - and others - to understand the problems the project
attempts to solve and the constraints within which the solution has to operate. 

To capture the architecture I use the [C4 modelling notation](https://c4model.com/) and [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language).

## Proposed Solution Overview

* [Context View (C4)](./a-context-view.md)
* [Container View (C4)](./a-container-view.md)
* [Security Considerations](./security.md)

## Other Things to Consider

* [Interactions Map](./interactions.md)
* [Data Exchange Network](./den.md)

### Software Development Kit (SDK)

The SDK is outside of the TopoSearch Network system. It is intended to be used by service developers to help with the rapid development of endpoint implementing the agreed search protocol. 

