# Open Distributed Information System - Server

The functionality can be split into a number of separate areas: 
* [Administration of the netwrok](#network)
* [Search and its federation](#search)
* [Handling of the feedback](#feedback) 
* [Data Catalogue](#data-catalogue)
* [Service Catalogue](#service-catalogue)

All of the above will be implemented as independent django applications.

While both the leaf services and the federation nodes will use the same API for 
key functionality, they could be implemented differently. 
This will allow the service developers a choice of level of functionality 
they want to offer their users. 

## How to run the service

Clone the repository and copy the template settings to `local.py`. 

```shell
cp code/local.template code/server/cofing/settings/local.py
```

Open the `local.py` file and enter a new random value for `SECRET_KEY`. 

```shell
pipenv shell
pipenv sync
cd code/server
python3 manage.py migrate
python3 manage.py runserver
```

open `127.0.0.1:8001` in a web browser


&nbsp;
# Details

&nbsp;
## Network

&nbsp;
## Search

&nbsp;
## Feedback

&nbsp;
## Data Catalogue

&nbsp;
## Service Catalogue