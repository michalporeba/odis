# Security Considerations

The key element of the proposed distributed data exchange network, 
as well as its biggest problem, is trust.

Sensitive and confidential data exchange and sharing in a federated environment is difficult. 
The most common solution, a central authorisation (if not authentication) provider, is not a likely option. 

## Scenarios

There four distinct scenarios, modes of operation, that may require different security solutions. 

&nbsp; 
### Public (mostly) Anonymous User

The users with none, or weak identity may have legitimate need and right to access public data. 
This should be made available easily with just enough protections to protect the integrity of the service, rather than the data. The security will work on Level 1 - the service. 

There should be no need for authorisation, but it might be necessary to authenticate users
for the purpose of rate limiting and similar. 

This is to suppor the [unauthenticated flow](./interactions.md#unauthenticated-flow).

&nbsp;
### Public Trusted User

Users with a strong identity guarantees may be authorised to access informaiton about the resources
they own across multiple organisations. It is Level 3 of the API access control. 

There are three potential solutions: 
1. Have individual organisation trust the central, strong identity provider. 
  (This would require not only the centralised trust, but also cooperation from 
  the teams maintaining the identity service).
1. Exchanging token in each organisation providing search (perhaps using SAML 2.0). 
1. Depend on Open ID Connect extension to OAuth 2.0 (ignoring authorisation).

This is to support the [Fine me use case](./usecases/findme.md) or the [authenticated flow](./interactions.md#authenticated-flow).

&nbsp;
### Internal Users

Internal users within the organisation could leverage the existing authentication and authorisation mechanisms. 


&nbsp;
### Federated Users

Access for trusted third organisations most likely will have to be solved by token exchange. 
The obvious problem with this solution is the amount of token exchanges that have to happen. 
There is also the issue of trust delegation described below. 

But first, the problem could be simplified by agreeing that across organisational boundaries
the access controls are simplified. The organisation agreeing to share the information 
controls access organisation by organisation. The specific user access is controlled 
on the site initiating the requests but in a way that both sides of the search transaction
can monitor the use. 

&nbsp; 
## Delegation of Trust

The topology of the search network is important to provide the context of the search
(that is the hypothesis behind this project). But the topology may become complex. 
Search (or data exchange) nodes can be chained between organisational units, and accross 
organisational boundaries. Strong controlls will be needed, and clear, transparent explanation
of what is going to happen if data is connected to and searchable from a given node. 

This remains a core problem that will have to be solved!

&nbsp;
## Standard Solutions 

Luckily, all of the above problems are not new. The security of similar systems 
have been well studied and many of the problems solved. 

This project will most likely apply the following
* [OAuth 2.0](https://oauth.net/2/) - to solve the authorisation issues.
* [Open ID Connect (OIDC)](https://openid.net/connect/) - an extension to OAuth 2.0 that deals with authentication. 
* [SAML 2.0](https://en.wikipedia.org/wiki/SAML_2.0) - to help authorisation across organisational boundaries. 
* [Signed JSON Web Tokens (JWS)](https://jwt.io/introduction) - which will serve as tokens in OAuth 2.0
* [Encrypted JSON Web Tokens (JWE)](https://datatracker.ietf.org/doc/html/rfc7516) - to help with end-to-end security in [zero-trust](https://en.wikipedia.org/wiki/Zero_trust_security_model) networks. 

All of the above solutions can be developed and implemented separately to the design 
and development of the service core functionality and so will be added in later stages. 
Not as afterthought, but as a planned improvement. Unless I can prove value of the 
proposed open, decentralised, data exchange network, there will be no need to secure it. 