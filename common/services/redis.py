import aioredis
from aioredis import Redis

from common.config import redis_settings


async def get_redis() -> Redis:
    """
    Функция, возвращающая уже подключенный объект к Redis-хранилищу.

    Returns:
        `Redis` - объект, предоставляющий интерфейс к Redis-хранилищу.
    """
    return await aioredis.from_url(
        redis_settings.redis_url,
        encoding="utf-8",
        db=redis_settings.db,
        decode_responses=True,
    )
