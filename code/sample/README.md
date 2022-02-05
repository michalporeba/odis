# The Sample Data Source

The service can provide and search in a few data sets. 
Each data set has multiple versions to pretend there 
are multiple services for demonstrations and testing. 

## How to run the service

Ensure your `hosts` file has `local.test` pointing at `127.0.0.1`.

Clone the repository and copy the template settings to `local.py`. 

```shell
cp code/local.template code/sample/cofing/settings/local.py
```

Open the `local.py` file and enter a new random value for `SECRET_KEY`. 

```shell
pipenv shell
pipenv install
cd code/sample
python3 manage.py migrate
python3 manage.py seed
python3 manage.py runserver
```

or `make run`

open `local.test:8000` in a web browser


## Available test data

There are three endpoints seeded with static test data, so that the tests
and demos can be easily repeated between environments. 

* `http://local.test:8000/cars/` contains fake car ownership data
* `http://local.test:8000/employment/` contains fake employment history data
* `http://local.test:8000/licenses/` contains fake driving license records

The records are constructed from [pregenerated fake data](./sample/people/data/). 
The [sample.json](./sample/people/data/sample.json) file is a specification of how to build the data and can be 
examined to see what records we should have about each person. 
