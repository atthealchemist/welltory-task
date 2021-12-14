from fastapi import HTTPException, status
from pydantic.types import UUID4

from common.models.task import TaskModel


class TaskNotFound(HTTPException):
    def __init__(self, task_id: UUID4) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with task id {task_id} was not found!",
            headers={},
        )


class TaskCreationError(HTTPException):
    def __init__(self, task: TaskModel) -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error when creating task: {task}",
            headers={},
        )
