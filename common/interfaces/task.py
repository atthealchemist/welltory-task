from abc import ABCMeta, abstractmethod
from typing import List, Union

from pydantic.types import UUID4

from common.enums.task import TaskStatus
from common.models.task import TaskModel


class TaskRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    async def add(self, task: TaskModel) -> None:
        """
        Добавить задачу в хранилище.

        Args:
            `task: TaskModel` - задача, которую планируется добавить в хранилище.
        """

    @abstractmethod
    async def get(self, task_id: UUID4) -> Union[TaskModel, bool]:
        """
        Получить задачу из хранилища по её идентификатору

        Args:
            `task_id: UUID4` - уникальный идентификатор задачи в формате UUID4

        Returns:
            `TaskModel` - объект задачи, если она найдена, иначе `False`
        """

    @abstractmethod
    async def delete(self, task_id: UUID4) -> bool:
        """
        Удалить задачу из хранилища по её идентификатору

        Args:
            `task_id: UUID4` - уникальный идентификатор задачи в формате UUID4

        Returns:
            `bool` - статус удаления - `True`, если удалена из хранилища, `False` - если возникли ошибки.
        """

    @abstractmethod
    async def update_status(self, task_id: UUID4, status: TaskStatus) -> None:
        """
        Обновление статуса задачи по её uuid

        Args:
            `task_id: UUID4` - уникальный идентификатор задачи в формате UUID4
            `status: TaskStatus` - новый статус задачи
        """

    @abstractmethod
    async def list_all(self) -> List[TaskModel]:
        """
        Список всех задач, находящихся в очереди.

        Returns:
            `List[TaskModel]` - список всех задач
        """
