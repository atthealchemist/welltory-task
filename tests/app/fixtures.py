import pytest
from fastapi.testclient import TestClient

from app.core.dependencies import get_tasks_repository
from app.main import app
from common.enums.task import TaskStatus
from common.models.task import (
    TaskCreate,
    TaskCreateResponse,
    TaskDeleteResponse,
    TaskModel,
)


@pytest.fixture
def client(fake_task_repository):
    app.dependency_overrides[get_tasks_repository] = lambda: fake_task_repository
    return TestClient(app)


@pytest.fixture
def task_create_payload():
    return TaskCreate(title="Sample Task", duration=30)


@pytest.fixture
def task_create_response_payload(task_fake_uuid):
    return TaskCreateResponse(id=task_fake_uuid)


@pytest.fixture
def task_delete_response_payload(task_fake_uuid):
    return TaskDeleteResponse(id=task_fake_uuid, deleted=True)


@pytest.fixture
def task_model_factory(task_fake_uuid):
    def new(
        title: str = "Sample Task",
        duration: int = 1,
        status: TaskStatus = TaskStatus.IDLE,
    ):
        return TaskModel(
            id=task_fake_uuid,
            title=f"{title} {task_fake_uuid}",
            duration=duration,
            status=status,
        )

    return new
