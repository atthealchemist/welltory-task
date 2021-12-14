from aioredis import Redis
from fastapi import Depends

from common.services.redis import get_redis
from common.services.tasks import TaskRepository


async def get_tasks_repository(redis: Redis = Depends(get_redis)):
    return TaskRepository(redis=redis)
