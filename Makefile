install:
	poetry install

make lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml