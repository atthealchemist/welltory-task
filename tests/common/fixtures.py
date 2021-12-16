import uuid

import pytest

from common.enums.task import TaskStatus
from common.models.task import TaskModel


@pytest.fixture
def task_fake_uuid():
    return uuid.uuid4()


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
