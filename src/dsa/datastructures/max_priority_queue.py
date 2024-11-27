"""Abstract class for max priority queue."""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class MaxPriorityQueue(ABC, Generic[T]):
    @abstractmethod
    def get_max(self) -> T:
        pass

    @abstractmethod
    def extract_max(self) -> T:
        pass

    @abstractmethod
    def insert(self, v: T) -> None:
        pass

    @abstractmethod
    def increase_key(self, k) -> None:
        pass

