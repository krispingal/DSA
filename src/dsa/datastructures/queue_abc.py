"""Queue abstract class"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class QueueABC(ABC, Generic[T]):
    @abstractmethod
    def enqueue(self, v: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass
