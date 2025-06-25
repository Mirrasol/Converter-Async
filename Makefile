install:
	uv sync

run:
	uv run uvicorn main:app --reload

test:
	uv run pytest -v tests/

lint:
	uv run ruff check

fix-lint:
	uv run ruff check --fix . 

build:
	uv build