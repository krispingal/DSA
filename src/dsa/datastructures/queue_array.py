"""Queue implemented using arrays/lists."""
from typing import TypeVar, Generic
from queue import Queue as QueueABC
T = TypeVar('T')


class Queue(QueueABC, Generic[T]):
    def __init__(self) -> None:
        self.items = []

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
    try:
        while True:
            print(q.dequeue())
    except IndexError:
        pass
