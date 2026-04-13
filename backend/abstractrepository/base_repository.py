from abc import ABC, abstractmethod
from typing import Generic, TypeVar

ModelType = TypeVar("ModelType")


class BaseRepository(ABC, Generic[ModelType]):
    @abstractmethod
    def get_by_id(self, entity_id: int) -> ModelType | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[ModelType]:
        raise NotImplementedError
