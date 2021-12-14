import asyncio
import logging

from aiologger import Logger

from common.enums.task import TaskStatus
from common.models.task import TaskModel
from common.services.redis import get_redis
from common.services.tasks import TaskRepository
from worker.interfaces.worker import WorkerInterface

logging.basicConfig(format="%(asctime)-8s %(message)s")


class TaskWorker(WorkerInterface):
    """
    Воркер, обрабатывающий задачи.
    """

    async def process_task(self, task: TaskModel) -> None:
        """
        Производим обработку конкретной задачи.

        Args:
            `task: TaskModel` - объект задачи.
        """
        duration = task.duration
        self._logger.info(f"Task {task.id} {TaskStatus.PROCESSING}")
        await self._repo.update_status(task_id=task.id, status=TaskStatus.PROCESSING)
        await asyncio.sleep(duration)
        if duration == 13:
            self._logger.info(f"Task {task.id} {TaskStatus.FAILED}")
            await self._repo.update_status(task_id=task.id, status=TaskStatus.FAILED)
        else:
            self._logger.info(f"Task {task.id} {TaskStatus.FINISHED}")
            await self._repo.update_status(task_id=task.id, status=TaskStatus.FINISHED)

    async def run(self) -> None:
        self._logger.info("Started worker, waiting for tasks")
        while True:
            tasks = await self._repo.list_all()
            for task in tasks:
                if task.status == TaskStatus.IDLE:
                    await self.process_task(task)

    def start(self) -> None:
        asyncio.run(self.run())

    def __init__(self) -> None:
        self._loop = asyncio.get_event_loop()
        self._redis = self._loop.run_until_complete(get_redis())
        self._repo = TaskRepository(redis=self._redis)
        self._logger = Logger.with_default_handlers(name=self.__class__.__name__)
