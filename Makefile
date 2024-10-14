mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

flush:
	python3 manage.py flush --no-input

load_data:
	python3 manage.py loaddata country.json
	python3 manage.py loaddata user.json

celery:
	celery -A root worker -l INFO

check:
	flake8 .
	isort .
