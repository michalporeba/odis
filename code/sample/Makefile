run: 
	pipenv sync
	python manage.py makemigrations
	python manage.py migrate 
	python manage.py seed
	python manage.py runserver