import asyncio

from common.services.redis import get_redis
from common.services.tasks import TaskRepository
from worker.task_worker import TaskWorker


async def main():
    redis = await get_redis()
    worker = TaskWorker(repository=TaskRepository(redis=redis))
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
