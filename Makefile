install-requirements:
	pip install -r requirements.txt

init-database:
	python3 manage.py db init 
	python3 manage.py db migrate
	python3 manage.py db upgrade

start:
	python3 manage.py run

run-formatter:
	autopep8 --recursive --in-place --max-line-length 79 --aggressive --aggressive app
	autopep8 --in-place --max-line-length 79 --aggressive --aggressive manage.py

run-linters:
	flake8 app/ manage.py

run-test-coverage:
	pytest --cov-report term-missing --cov=app app/test/

fixtures:
	pytest --fixtures app/test

seed-database-list:
	python3 manage.py seed list

seed-database:
	python3 manage.py seed run
