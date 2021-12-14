from enum import Enum


class TaskStatus(str, Enum):
    """
    Статусы задачи.

    Variants:
        `IDLE` - задача создана, но ещё не была запущена.

        `PROCESSING` - задача запущена, выполняется.

        `FAILED`- задача завершилась с ошибкой.

        `FINISHED` - задача завершилась успешно.

    """

    IDLE = "idle"
    PROCESSING = "processing"
    FAILED = "failed"
    FINISHED = "finished"

    def __str__(self) -> str:
        return self.value
