# Notes 

https://github.com/awesomedata/awesome-public-datasets

## Possible use cases

### Food and drink as department surrogate

http://snap.stanford.edu/data/ - a collection of data. There are online reviews for beers, wines, movies and foods. Perhaps this sort of data could represent different departments interested in slightly different things. A search from a department of beers would return beer first, and then show wines and others and so on. 

### Open UK Data 

Searching for physical locations in public datasets https://data.gov.uk/
Could result in aggregated results, but feedback would be difficult to show. 

## API Designß

* [Mike Amundsen - Twelve Patterns for Evolvable Web APIs](https://www.youtube.com/watch?v=qolWrn7hNro) - a lot of good ideas how to design interactions
*TBC*

## Python / Django techniques

* [Reusable Django Apps](https://docs.djangoproject.com/en/4.0/intro/reusable-apps/)
* [Extensible and reusable Django applications](https://www.philipotoole.com/reusable-django-applications/)
* [Celery to communicate between apps?](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
* [Reusable Apps on YouTube](https://www.youtube.com/watch?v=A-S0tqpPga4)

### A pub/sub or messagebus could be used for communication between apps.
* [PyDispatcher](http://pydispatcher.sourceforge.net/)
* [DjangoPubSub](https://pypi.org/project/djangopubsub/)
* [PyPubSub](https://pypubsub.readthedocs.io/en/v4.0.3/)


## Search options to consider

* [Collaborative Search](https://en.wikipedia.org/wiki/Collaborative_search_engine)
* [Enterprise Search](https://en.wikipedia.org/wiki/Enterprise_search)
* [Semantic Search](https://en.wikipedia.org/wiki/Semantic_search)

## Search tools to consdier

* [Apache Solr](https://solr.apache.org/features.html)
* Windows 7+, Sharepoint, Bing

## Problems that need solving

* The UI has to be progressive and usable with no client side scripting. At the same time the service needs to be ReSTful. How can we return the aggregated results and allow users to drill down to the detail and send feedback? With a single page application it would be easier, as all the infromation could be returned and manipulated on the client side for display, but this cannot be the only option. 


## Packaging 

https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f



&nbsp;
# Common questions that need answering

## What problems does service to service negotiation sovle? 
Typically, as a developer, I know exactly what API I need, which one I want to use
and might as well read the documentation and use it. 

The above question shows only half of the problem, how to consume APIs. 
The other half of the problem is how to provide a service through an API. 
How to offer those services on the scale of decades without tight coupling. 