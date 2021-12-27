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