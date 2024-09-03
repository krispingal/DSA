"""Stack implementation using linked list."""
from typing import TypeVar, Generic
from linked_list import Node
from stack import Stack as StackABC

T = TypeVar('T')


class Stack(StackABC, Generic[T]):
    def __init__(self) -> None:
        self.head = None

    def push(self, val: T) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self) -> T:
        if self.is_empty(): raise IndexError
        pop_val = self.head.val
        self.head = self.head.next
        return pop_val

    def is_empty(self) -> bool:
        return not self.head

    def peek(self) -> T:
        if not self.head: return
        return self.head.val

   
if __name__ == '__main__':
    stack = Stack()
    lis = "All that glitters is not gold".split(" ")[::-1]
    for a in lis:
        stack.push(a)
    while not stack.is_empty():
        print(stack.pop())
