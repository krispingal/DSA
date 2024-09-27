"""Linked list implementation."""
from typing import TypeVar, Generic

T = TypeVar('T')


class ListNode(Generic[T]):
    def __init__(self, val: T, next=None) -> None:
        self.val = val
        self.next: ListNode | None = next


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = None

    def prepend(self, val: T) -> None:
        """Inserts a node at the beginning of the list."""
        new_node = ListNode(val, self.head)
        self.head = new_node

    def append(self, val: T) -> None:
        """Inserts a node at the end of the list."""
        if not self.head:
            self.head = ListNode(val, None)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val, None)

    def insert_at_position(self, position: int, val: T) -> bool:
        """Inserts a node at a specific position."""
        if position < 0:
            return False
        if position == 0:
            new_node = ListNode(val, self.head)
            self.head = new_node
            return True
        cur = self.head
        while cur.next and position - 1 > 0:
            cur = cur.next
            position -= 1
        if position == 1:
            temp = cur.next
            cur.next = ListNode(val, temp)
            return True
        return False # Linked list cannot insert element without any preceding elements.

    def delete_by_value(self, key: T) -> bool:
        """Deletes the first occurrence of the node containing data."""
        cur, prev = self.head, None
        while cur:
            if cur.val == key:
                if prev:
                    prev.next = cur.next
                else:
                    self.head =cur.next
                return True
            cur, prev = cur.next, cur
        return False

    def delete_at_position(self, position: int) -> bool:
        """Deletes a node at a specific index."""
        if position < 0 or not self.head:
            return False
        cur, prev = self.head, None
        while cur and position > 0:
            cur, prev = cur.next, cur
            position -= 1
        if cur and position == 0:
            if not prev:
                self.head = self.head.next
            else:
                prev.next = cur.next
            return True
        return False


    def search(self, key: T) -> bool:
        """Search the list for presence of key."""
        cur = self.head
        while cur and cur.val != key:
            cur = cur.next
        return True if cur and cur.val == key else False

    def get_node_at(self, index) -> T:
        """Returns the node at the given index."""
        if index < 0:
            return None
        cur = self.head
        while cur and index > 0:
            index -= 1
            cur = cur.next
        return cur.val if cur else None

    def display(self) -> None:
        """Prints out the entire list."""
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()



    def reverse(self):
        """Reverses the linked list."""
        # TODO
        pass
