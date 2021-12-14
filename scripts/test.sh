#! /usr/bin/env bash

# Exit in case of error
set -e
make generate_dot_env
docker-compose up --build -d
docker-compose exec app pytest -vv --show-capture=all $@  