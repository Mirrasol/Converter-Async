install:
	uv sync

run:
	uv run uvicorn main:app

test:
	uv run pytest -v app/test/

lint:
	uv run flake8 app

build:
	uv build