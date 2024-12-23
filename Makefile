install:
	uv sync

run:
	uv run main:app

test:
	uv run pytest -v app/test/

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

lint:
	uv run flake8 app

build:
	uv build