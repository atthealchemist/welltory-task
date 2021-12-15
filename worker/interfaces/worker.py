from abc import ABCMeta, abstractmethod


class WorkerInterface(metaclass=ABCMeta):
    """
    Интерфейс для создания воркеров.
    """

    @abstractmethod
    async def run(self):
        """
        Логика работы конкретного воркера находится здесь.
        """
