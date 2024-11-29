"""Stack implemented using Arrays/lists"""

from dataclasses import dataclass, field
from typing import TypeVar, Generic
from src.dsa.datastructures.stack_abc import Stack as StackABC

T = TypeVar("T")


@dataclass
class Stack(StackABC, Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError
        return self.items.pop()

    def is_empty(self) -> bool:
        return not self.items

    def peek(self) -> T:
        return self.items[-1]


if __name__ == "__main__":
    stack = Stack()
    lis = "All that glitters is not gold".split(" ")[::-1]
    for a in lis:
        stack.push(a)
    print(stack)
