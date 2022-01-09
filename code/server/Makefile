shell:
	pipenv sync
	pipenv shell 
	
demo1:
	python manage.py migrate --database=demo1
	python manage.py seed --settings=config.settings.demo1 --silent
	python manage.py runserver 8081 --settings=config.settings.demo1

demo2:
	python manage.py migrate --database=demo2
	python manage.py seed --settings=config.settings.demo2 --silent
	python manage.py runserver 8082 --settings=config.settings.demo2

demo3: 
	python manage.py migrate --database=demo3
	python manage.py seed --settings=config.settings.demo2 --silent
	python manage.py runserver 8083 --settings=config.settings.demo3

run: 
	python manage.py migrate 
	python manage.py seed --settings=config.settings.dev --silent
	python manage.py runserver