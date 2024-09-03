"""Queue implemented using linked list."""
from typing import TypeVar, Generic
from linked_list import Node
from queue import Queue as QueueABC


T = TypeVar('T')


class Queue(QueueABC, Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, val: T) -> None:
        nnode = Node(val)
        if not self.tail:
            self.head = self.tail = nnode
        else:
            self.tail.next = nnode
            self.tail = nnode

    def dequeue(self) -> T:
        if self.is_empty(): raise IndexError
        val, self.head = self.head.val, self.head.next
        return val

    def is_empty(self) -> bool:
        return not self.head

    def peek(self) -> T:
        if self.is_empty(): raise IndexError
        return self.head.val


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
