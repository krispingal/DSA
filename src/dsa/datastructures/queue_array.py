"""Queue implemented using arrays/lists."""
from dataclasses import dataclass, field
from typing import TypeVar, Generic
from src.dsa.datastructures.queue_abc import QueueABC
T = TypeVar('T')


@dataclass
class Queue(QueueABC, Generic[T]):
    items: list[T] = field(default_factory=list)
    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if self.is_empty(): raise IndexError
        # The following is an O(n) operation
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return not self.items

    def peek(self) -> T:
        if self.is_empty(): raise IndexError
        return self.items[0]


if __name__ == '__main__':
    q = Queue()
    lis = "All that glitters is not gold".split(" ")
    for a in lis:
        q.enqueue(a)
    print(q)
