from typing import List

from pydantic import BaseModel

from common.enums.task import TaskStatus
from common.models.base import IdentifiedModel


class TaskCreate(BaseModel):
    """
    Запрос на создание задачи

    Attributes:
        `title: str` - человеко-понятное название задачи
        `duration: int` - время выполнения задачи (в секундах)
    """

    title: str
    duration: int


class TaskCreateResponse(IdentifiedModel):
    """
    Ответ на запрос о создании задачи.

    Attributes:
        `uuid: UUID4` - уникальный идентификатор задачи
    """


class TaskDeleteResponse(IdentifiedModel):
    """
    Ответ на запрос об удалении задачи

    Attributes:
        `uuid: UUID4` - уникальный идентификатор задачи
        `deleted: bool` - флаг, показывающий, что задача была действительно удалена.
    """

    deleted: bool


class TaskModel(IdentifiedModel):
    """
    Модель задачи.

    Attributes:
        `id: UUID4` - уникальный идентификатор задачи в формате UUID4
        `title: str` - человеко-понятное имя задачи
        `duration: int` - время исполнения задачи (в секундах)
        `status: TaskStatus` - статус исполнения задачи (IDLE по умолчанию)
    """

    title: str
    duration: int
    status: TaskStatus = TaskStatus.IDLE


class TaskListResponse(BaseModel):
    """
    Ответ на запрос о получении списка задач.

    Attributes:
        `tasks: List[TaskModel]` - список задач
    """

    tasks: List[TaskModel]
