SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

ifeq ($(TIMEOUT),)
TIMEOUT := 60
endif

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: generate_dot_env all clean test install run deploy down worker

all: generate_dot_env clean test install run deploy down worker

test:
	poetry run python -m pytest tests -vv --show-capture=all

install: 
	generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry install

run:
	poetry run python app/main.py

worker:
	poetry run celery -A tasks worker --loglevel=INFO

deploy: 
	generate_dot_env
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf __pycache__
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build