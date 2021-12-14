import uuid

import pytest

from common.models.task import (TaskCreate, TaskCreateResponse,
                                TaskDeleteResponse)


@pytest.fixture
def task_fake_uuid():
    return uuid.uuid4()


@pytest.fixture
def task_create_payload():
    return TaskCreate(title="Sample Task", duration=30).json()


@pytest.fixture
def task_create_response_payload(task_fake_uuid):
    return TaskCreateResponse(id=task_fake_uuid).json()


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
