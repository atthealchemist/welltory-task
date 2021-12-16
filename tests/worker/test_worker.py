from unittest.mock import AsyncMock

import pytest

from common.enums.task import TaskStatus


class TestWorker:
    async def fake_worker_run(self, fake_task_repository):
        tasks = await fake_task_repository.list_all()
        for task in tasks:
            if task.status == TaskStatus.IDLE:
                await self.fake_process_task(task, fake_task_repository)

    async def fake_process_task(self, task, fake_task_repository):
        duration = task.duration
        await fake_task_repository.update_status(
            task_id=task.id, status=TaskStatus.PROCESSING
        )
        asyncio = AsyncMock()
        asyncio.sleep.return_value = True
        await asyncio.sleep(duration)
        if duration == 13:
            await fake_task_repository.update_status(
                task_id=task.id, status=TaskStatus.FAILED
            )
            return
        await fake_task_repository.update_status(
            task_id=task.id, status=TaskStatus.FINISHED
        )

    @pytest.mark.asyncio
    async def test_worker_all_tasks_finished(self, fake_task_repository, fake_worker):
        fake_worker.run.side_effect = self.fake_worker_run
        await fake_worker.run(fake_task_repository)
        tasks = await fake_task_repository.list_all()
        assert all([t for t in tasks if t.status == TaskStatus.FINISHED])

    @pytest.mark.asyncio
    async def test_worker_thirteen_task_failed(
        self, fake_task_repository_factory, task_model_factory, fake_worker
    ):
        fake_task_repository = fake_task_repository_factory(
            task_model_factory(), task_model_factory(duration=13)
        )
        fake_worker.run.side_effect = self.fake_worker_run
        await fake_worker.run(fake_task_repository)
        tasks = await fake_task_repository.list_all()
        assert any([t for t in tasks if t.status == TaskStatus.FAILED])
