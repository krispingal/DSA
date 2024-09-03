"""Linked list implementation."""
from typing import TypeVar, Generic

T = TypeVar('T')


class ListNode(Generic[T]):
    def __init__(self, val: T, next=None) -> None:
        self.val = val
        self._next: ListNode | None = next


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = None

    def insert(self, val: T) -> None:
        """Inserts new node at the beginning"""
        new_node = ListNode(val, self.head)
        self.head = new_node

    def search(self, key: T) -> ListNode | None:
        """Search the list for presence of key."""
        cur = self.head
        while cur and cur.val != key:
            cur = cur._next
        return cur

    def delete(self, pos: int) -> None:
        cur = self.head
        if not cur: return
        while cur and cur._next and cur._next.val != key:
            cur = cur._next
        if not cur or not cur._next: return


if __name__ == '__main__':
    lis = LinkedList()
    for a in range(15):
        lis.insert(a)
    v = lis.search()

