mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

flush:
	python3 manage.py flush --no-input

load_data:
	python3 manage.py loaddata country.json
	#python3 manage.py loaddata user.json

user:
	python3 manage.py createsuperuser --email admin@gmail.com

celery:
	celery -A root worker -l INFO

check:
	flake8 .
	isort .

fake:
	python3 manage.py generate_data --user 5
	python3 manage.py generate_data --address 5
	python3 manage.py generate_data --book 5
	python3 manage.py generate_data --author 5

migdel:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
