# Architectural Decision Record

The relevant architectural decisions will be recorded here


### 2021-12-14

**Existing Search Standards** #ISSUE-4 - OpenSearch will be used on the periphery on the search network and a new API will be designed for the internal collaboration between the nodes. 

### 2021-12-16

**HATEOAS** #ISSUE-2 - There should be no need to really choose specific style
of the HATEOAS implementation and mulitple common formats will be supported. 

### 2021-12-26

**API Security** - API Security should not be a separate part to the API design. 
It will be implemented using standards: SAML 2.0, OAuth 2.0 and OIDC. 
Security should be handled as prescribed by those standards, and not included
in the API data model - which will allow flexibility (see above). 

### 2022-01-02

**WSTL** - I will base the internal state transition representation on the [WSTL](http://rwcbook.github.io/wstl-spec/) draft spec. That also means, that the service by default
will produce the data in the WSTL format. 


### 2022-01-05

**Registry-Dispatcher** - To allow low-friction integration of my service components
with services developed with Django, as well as any other python frameworks
I will use combination of [registry and dispatcher](../code/scratchpad/plugins/) patterns 
to implement communication between components.

### 2021-01-06

**Norman's Action Lifecycle** - To ensure good API design I will use 
the [Action Lifecycle](https://en.wikipedia.org/wiki/Human_action_cycle)
model, possibly in the [Reaquest, Parse, Wait (RPW)](https://medium.com/pragmatic-programmers/understanding-normans-action-lifecycle-b705a9ab9aa9) simplification proposed by M. Amundsen.