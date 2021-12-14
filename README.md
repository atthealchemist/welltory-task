# welltory-task

Test tasks for Welltory

---
[![BCH compliance](https://bettercodehub.com/edge/badge/atthealchemist/welltory-task?branch=master)](https://bettercodehub.com/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/36b4ea4a54b144968028c2ec61047690)](https://www.codacy.com/gh/atthealchemist/welltory-task/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=atthealchemist/welltory-task&amp;utm_campaign=Badge_Grade)
---
## Technology stack
- Docker (with Docker Compose)
- Python 3.8+
    - FastAPI
    - Celery
    - aioredis
- Redis

All of them were updated to their **latest stable** versions

## Installation

```bash
git clone https://github.com/atthealchemist/welltory-task.git
cd welltory-task
```

## Commands
|Description |Local        |Docker               |
|------------|------------ |---------------------|
|Run app     |`make run`   |`./scripts/run.sh`   |
|Run tests   |`make test`  |`./scripts/test.sh`  |
|Deploy app  |`make deploy`|`./scripts/deploy.sh`|

## API Documentation
- Swagger version - http://localhost:8080/api/v1/docs
- Redoc version - http://localhost:8080/api/v1/redoc

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:
```
.
├── app                        - Main application service with api
├── conftest.py                - Test configuration for all serivces
├── docker-compose.yml
├── Dockerfile
├── common                      - Common logic for all services
├── Makefile                    - Helper scripts for services locally
├── poetry.lock
├── pyproject.toml
├── README.md
├── scripts                      - Helper scripts for services in Docker
├── tests                        - Tests folder with tests separated by service
└── worker                       - Worker service
```