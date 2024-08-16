"""Stack implemented using Arrays/lists"""
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.is_empty(): raise IndexError
        return self.items.pop()

    def is_empty(self) -> bool:
        return not self.items
    
    def peek(self) -> T:
        return self.items[-1]

if __name__ == '__main__':
    stack = Stack()
    lis = "All that glitters is not gold".split(" ")[::-1]
    for a in lis:
        stack.push(a)
    while not stack.is_empty():
        print(stack.pop())