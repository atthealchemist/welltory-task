from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class IdentifiedModel(BaseModel):
    """
    Базовая модель с идентификатором (UUID4)

    Attributes:
        `id: UUID` - идентификатор, по умолчанию равен случайному значению из `uuid.uuid4()`
    """

    id: UUID = Field(default_factory=uuid4)
