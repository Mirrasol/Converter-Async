install:
	uv sync

run:
	uv run uvicorn main:app --reload

test:
	uv run pytest -v tests/

lint:
	uv run flake8 app

build:
	uv build