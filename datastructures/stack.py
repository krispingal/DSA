"""Stack implementation using linked list."""
from linked_list import Node


class Stack:
    def __init__(self):
        self.head = None

    def top(self):
        if not self.head: return
        return self.head.val

    def push(self, val: object) -> None:
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self) -> object:
        if not self.head: raise StopIteration
        pop_val = self.head.val
        self.head = self.head.next
        return pop_val

if __name__ == '__main__':
    stack = Stack()
    lis = "All that glitters is not gold".split(" ")[::-1]
    for a in lis:
        stack.push(a)
    while stack.top():
        print(stack.pop())
