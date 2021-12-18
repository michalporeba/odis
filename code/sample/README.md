# The Sample Data Source

The service can provide and search in a few data sets. 
Each data set has multiple versions to pretend there 
are multiple services for demonstrations and testing. 

## How to run the service

Clone the repository and copy the template settings to `local.py`. 

```shell
cp code/local.template code/sample/cofing/settings/local.py
```

Open the `local.py` file and enter a new random value for `SECRET_KEY`. 

```shell
pipenv shell
cd code/sample
python3 manage.py migrate
python3 manage.py seed
python3 manage.py runserver
```

open `127.0.0.1:8000` in a web browser


