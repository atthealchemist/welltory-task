import json
from typing import List, Union

from aioredis import Redis
from pydantic.types import UUID4

from common.enums.task import TaskStatus
from common.interfaces.task import TaskRepositoryInterface
from common.models.task import TaskModel


class TaskRepository(TaskRepositoryInterface):
    """
    Хранение и получение задач из Redis
    """

    def __init__(self, redis: Redis):
        self._redis = redis

    async def add(self, task: TaskModel) -> None:
        serialized_task = task.json()
        return await self._redis.set(f"task:{task.id}", serialized_task)

    async def get(self, task_id: UUID4) -> Union[TaskModel, bool]:
        task_serialized = await self._redis.get(f"task:{task_id}")
        if not task_serialized:
            return False
        return TaskModel(**json.loads(task_serialized))

    async def update_status(self, task_id: UUID4, status: TaskStatus) -> None:
        task = await self.get(task_id)
        task.status = status
        await self.add(task)

    async def list_all(self) -> List[TaskModel]:
        cur = b"0"
        tasks = []
        while cur:
            cur, keys = await self._redis.scan(cur, match="task:*")
            for key in keys:
                _, uuid = key.split(":")
                task = await self.get(uuid)
                tasks.append(task)
        return tasks

    async def list_idle(self) -> List[TaskModel]:
        idle_tasks = []
        async for task in self.list_all():
            if task.status == TaskStatus.IDLE:
                idle_tasks.append(task)
        return idle_tasks

    async def delete(self, task_id: UUID4) -> bool:
        result = await self._redis.delete(f"task:{task_id}")
        return bool(result)
