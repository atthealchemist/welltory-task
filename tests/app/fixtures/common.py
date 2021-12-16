import pytest
from fastapi.testclient import TestClient

from app.core.dependencies import get_tasks_repository
from app.main import app


@pytest.fixture
def client(fake_task_repository):
    app.dependency_overrides[get_tasks_repository] = lambda: fake_task_repository
    return TestClient(app)
