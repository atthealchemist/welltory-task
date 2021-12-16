import asyncio
from unittest.mock import AsyncMock

import pytest

from worker.task_worker import TaskWorker


@pytest.fixture
def fake_worker(fake_task_repository):
    fake_worker = TaskWorker(repository=fake_task_repository)
    fake_worker.run = AsyncMock()
    return fake_worker


@pytest.fixture
def fake_task_repository(fake_task_repository_factory, task_model_factory):
    return fake_task_repository_factory(
        task_model_factory(), task_model_factory(), task_model_factory()
    )


@pytest.fixture
def fake_task_repository_factory(task_model_factory):
    def new(*tasks):
        repo = AsyncMock()

        def fake_update_status(task_id, status):
            task, *rest = [t for t in repo.list_all.return_value if t.id == task_id]
            task.status = status
            repo.list_all.return_value = [task, *rest]

        repo.list_all.return_value = [*tasks]
        repo.get.return_value = task_model_factory()
        repo.add.return_value = True
        repo.delete.return_value = True
        repo.update_status.side_effect = fake_update_status
        return repo

    return new


@pytest.fixture
def fake_tasks_list(fake_task_repository):
    return asyncio.get_event_loop().run_until_complete(fake_task_repository.list_all())
