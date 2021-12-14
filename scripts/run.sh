#! /usr/bin/env bash

# Exit in case of error
set -e
make generate_dot_env
docker-compose up -d