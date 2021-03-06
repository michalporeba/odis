# Project Log

## Week 0 - ending 2021-12-12

*A setup week, starting with necessary learning and such.*

### Features and tasks completed: 

* **Project Setup**
    * [Project monitoring](./progress.md) set up
    * GitHub project set up
    * Quick review of [search](https://github.com/michalporeba/odis/issues/4) and [HATEOAS](https://github.com/michalporeba/odis/issues/2) standards
* Search Standards (partial)
    * [High-level architecture design](./docs/architecture.md)
* Learn Django (partial)
    * [Quick Django introduction](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

&nbsp;

## Week 1 - ending 2021-12-19

*More learning*

### Features and tasks completed:

* **Learn Django**
    * [Two Scoops of Django 3.x](https://www.feldroy.com/books/two-scoops-of-django-3-x)
    * Server project create and modified to match TSD recommendations
* **Search Standards**
    * SRW/U and OpenSearch reviewed - decision logged in #ISSUE-4
    * [High-level architecture design](./docs/architecture.md)
* **HATEOAS**
    * Reviewed number of potential styles of hypermedia interfaces
    * Chose not to choose - decision logged in #ISSUE-2
* **Use Cases**
    * There are now [4 use cases](./docs/) documented

&nbsp;

## Week 2 - ending 2021-12-26

*Final week of gentle warmup to the project - mostly reading.*

### Features and tasks completed: 

* Security Considerations
    * Read [Solving Identity Management in Modern Applications](https://link.springer.com/book/10.1007/978-1-4842-5095-2)
    * Read [Advanced API Security](https://link.springer.com/book/10.1007/978-1-4302-6817-8)
    * Read [UK Digital Identity](https://gds.blog.gov.uk/2021/07/13/a-single-sign-on-and-digital-identity-solution-for-government/)

## Week 3 - ending 2022-01-02

*Finalising the principals for API design, including security.*

### Features completed: 

* Security Considerations
* API Design Considerations
* Universal Demo Project

## Week 4 - ending 2022-01-09

*Wrestling Python and Django internals*

I have attempted to build basic interactions between ODIS nodes this week. 
It proved more difficult than I expected, mostly due to clearly lack of knowledge 
in finer points of Python's type system, mutliple inheritance and metaprogramming.

The scope also expanded a little, as I realised testing further on will quickly 
become too difficult/time consuming if I don't invest now in some tooling. To help 
reduce burden further down the line, I have started a number of standalone packages:

* ALPS-PY
* Callout
* Django-Kinder-Settings
* Polymedia

## Week 5 - ending 2022-01-16

*Working on the supporting packages*

### Features completed: 

* ALPS
* Polymedia package

To help with development and testing of the ideas I have developed
* ALPS-PY - a package to create, parse and manage ALPS service descriptions
* Callout - a way to modularise odis without dependencies
* Diogi - a collection of functions to make my life easier
* Django-Kinder-Settings - a more developer friendly settings for django
* Polymedia - a client to communicate with hypermedia using ALPS 
* Poly-CLI - a command line interface for Polymedia - for testing


## Week 6 - ending 2022-01-23

Engagements, no feature complete. 

## Week 7 - ending 2022-01-31

Many more discussions both inside and outside of the organisation, but the only material progress is the proxy setup with mitmproxy to help with validation of the protocol.

## Week 8 - ending 2022-02-06

Fission UCAN Check - a potentially interesting project dealing with
distributed permissions by extending JWT. Interesting ideas on how to 
pass on authorisation with a chain of proofs. Distributed identity(ION is another option)

### Features completed: 

* Simple search federation (without aggregation)
* Open API considerations

## Week 9 - ending 2022-02-13

### Features completed: 

* Engagement with x-gov community

## Week 10 - ending 2022-02-21

### Features completed: 

* Public packages - 4