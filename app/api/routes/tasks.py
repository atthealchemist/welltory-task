from typing import List, Optional

from fastapi import APIRouter, Depends, Path, Response, status
from fastapi.param_functions import Query
from pydantic.types import UUID4

from app.core.dependencies import get_tasks_repository
from app.core.errors import TaskCreationError, TaskNotFound
from common.enums.task import TaskStatus
from common.models.task import (
    TaskCreate,
    TaskCreateResponse,
    TaskDeleteResponse,
    TaskModel,
)
from common.services.tasks import TaskRepository

router = APIRouter()


@router.get(
    "/{task_id}",
    response_model=TaskModel,
    name="tasks:get",
    summary="Получить задачу по её идентификатору",
)
async def get_task(
    task_id: UUID4 = Path(..., description="Уникальный идентификатор задачи"),
    tasks_repo: TaskRepository = Depends(get_tasks_repository),
):
    task = await tasks_repo.get(task_id=task_id)
    if not task:
        raise TaskNotFound(task_id=task_id)
    return task


@router.post("/", name="tasks:create", summary="Добавить новую задачу")
async def create_task(
    task: TaskCreate,
    response: Response,
    tasks_repo: TaskRepository = Depends(get_tasks_repository),
):
    new_task = TaskModel(**task.dict())
    is_created = await tasks_repo.add(new_task)
    if not is_created:
        raise TaskCreationError(task=new_task)
    response.status_code = status.HTTP_201_CREATED
    return TaskCreateResponse(id=new_task.id)


@router.get(
    "/", response_model=List[TaskModel], name="tasks:list", summary="Список всех задач"
)
async def list_tasks(
    tasks_repo: TaskRepository = Depends(get_tasks_repository),
    status: Optional[TaskStatus] = Query(None, description="Статус задачи"),
):
    tasks = await tasks_repo.list_all()
    if status:
        tasks = [t for t in tasks if t.status == status]
    return tasks


@router.delete(
    "/{task_id}",
    response_model=TaskDeleteResponse,
    name="tasks:delete",
    summary="Удалить задачу",
)
async def delete_task(
    task_id: UUID4 = Path(..., description="Уникальный идентификатор задачи"),
    tasks_repo: TaskRepository = Depends(get_tasks_repository),
):
    task = await tasks_repo.get(task_id=task_id)
    if not task:
        raise TaskNotFound(task_id=task_id)
    deleted = await tasks_repo.delete(task_id=task.id)
    return TaskDeleteResponse(id=task_id, deleted=deleted)
