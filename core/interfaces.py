from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional, Any

T = TypeVar('T')

class BaseRepositoryInterface(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: Any) -> Optional[T]:
        pass

    @abstractmethod
    def list_all(self) -> List[T]:
        pass

    @abstractmethod
    def create(self, **kwargs) -> T:
        pass

    @abstractmethod
    def update(self, id: Any, **kwargs) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, id: Any) -> bool:
        pass

class BaseServiceInterface(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
