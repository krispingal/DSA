"""Doubly Linked list implementation."""
from typing import TypeVar, Generic

T = TypeVar('T')


class ListNode(Generic[T]):
    def __init__(self, val: T, next=None, prev=None) -> None:
        self.val = val
        self._next: ListNode | None = next
        self._prev: ListNode | None = prev


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_beginning(self, val: T) -> None:
        """Inserts val to the head."""
        new_node = ListNode(val, self.head)
        if not self.head:
            self.tail = new_node
        else:
            self.head._prev = new_node
        self.head = new_node

    def insert_end(self, val: T) -> None:
        """Inserts val to the tail."""
        new_node = ListNode(val, None, self.tail)
        if not self.tail:
            self.head = new_node
        else:
            self.tail._next = new_node
        self.tail = new_node

    def traverse(self) -> None:
        """Traverses from the start to end."""
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur._next

    def search(self, val: T) -> ListNode | None:
        """Searches for key in linked list."""
        cur = self.head
        while cur and cur.val != val:
            cur = cur._next
        return cur

    def delete(self, node: ListNode) -> None:
        """Deletes a node from linked list."""
        if node._prev:
            node._prev._next = node._next
        else:
            self.head = node._next
        if node._next:
            node._next._prev = node._prev
        else:
            self.tail = node._prev


if __name__ == '__main__':
    dlinkList = DoublyLinkedList()
    for i in range(0, -5, -1):
        dlinkList.insert_beginning(i)
    for i in range(1, 5, 1):
        dlinkList.insert_end(i)
    dlinkList.traverse()
    print("Deleting -4 and 4 from linked list\n")

    x = dlinkList.search(4)
    dlinkList.delete(x)
    x = dlinkList.search(-4)
    dlinkList.delete(x)
    
    dlinkList.traverse()

