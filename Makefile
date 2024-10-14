mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

load_data:
	python3 manage.py loaddata country.json
	python3 manage.py loaddata user.json