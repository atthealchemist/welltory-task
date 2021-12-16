import json
import uuid

import pytest

from common.enums.task import TaskStatus
from common.models.task import (
    TaskCreate,
    TaskCreateResponse,
    TaskDeleteResponse,
    TaskModel,
)


@pytest.fixture
def task_fake_uuid():
    return uuid.uuid4()


@pytest.fixture
def task_create_payload():
    return json.loads(TaskCreate(title="Sample Task", duration=30).json())


@pytest.fixture
def task_create_response_payload(task_fake_uuid):
    return TaskCreateResponse(id=task_fake_uuid)


@pytest.fixture
def task_delete_response_payload(task_fake_uuid):
    return TaskDeleteResponse(id=task_fake_uuid, deleted=True)


@pytest.fixture
def task_get_payload(task_fake_uuid):
    return {
        "id": task_fake_uuid,
        "title": "Sample Task",
        "duration": 999,
        "status": "idle",
    }


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
