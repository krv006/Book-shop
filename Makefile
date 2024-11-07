mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

flush:
	python3 manage.py flush --no-input

migdel:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
load_data:
	python3 manage.py loaddata country.json
	#python3 manage.py loaddata user.json

user:
	python3 manage.py createsuperuser --email admin@gmail.com

celery:
	celery -A root worker -l INFO --concurrency=4 -Q high_priority -n worker1
	celery -A root worker -l INFO --concurrency=1 -Q low_priority -n worker3

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


data:
	python3 manage.py generate_data --user 5 --author 5  --address 5  --book 5  --section 5  --review 5 --category 5
	#python3 manage.py generate_data --user 5 --author 5  --address 5  --book 5  --section 5  --cart 5  --review 5 --category 5

seeder:
	python3 manage.py seed shops --number=10 # todo shops di orniga esa ozimizdi appimizdi yozamiz


#10.10.3.122:8000/api/v1/users/register?email=rvkamronbek@gmail.com