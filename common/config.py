from pathlib import Path

from pydantic import BaseSettings, Field

PROJECT_ROOT = Path(__file__).parents[1]


class Settings(BaseSettings):
    """
    Общий для всех сервисов базовый класс настроек.

    Аттрибуты настроек берутся из .env файла в корне проекта.
    """

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class RedisSettings(Settings):
    """
    Настройки для подключения к Redis.
    
    Attributes:
        `host: str` - доменное имя машины, на которой запущен Redis-сервер. 
        По умолчанию берётся из переменной `REDIS_HOST` в .env файле.
        `port: str` - доменное имя машины, на которой запущен Redis-сервер. 
        По умолчанию берётся из переменной `REDIS_PORT` в .env файле.
        `db: int` - идентификатор выбранной базы данных на Redis сервере.
        По умолчанию берётся из переменной `REDIS_DB` в .env файле.
    """

    host: str = Field(..., env="REDIS_HOST")
    port: int = Field(..., env="REDIS_PORT")
    db: int = Field(..., env="REDIS_DB")

    @property
    def redis_url(self):
        """
        Возвращается готовый url вида redis://localhost:6379
        """
        return f"redis://{self.host}:{self.port}"


redis_settings = RedisSettings()
