"""Doubly Linked list implementation."""

from typing import TypeVar, Generic

T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, val: T, next=None, prev=None) -> None:
        self.val = val
        self.next: ListNode | None = next
        self.prev: ListNode | None = prev


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def prepend(self, val: T) -> None:
        """Inserts val to the head."""
        new_node = ListNode(val, self.head)
        if not self.head:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node

    def append(self, val: T) -> None:
        """Inserts val to the tail."""
        new_node = ListNode(val, None, self.tail)
        if not self.tail:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def insert_at_position(self, position: int, val: T) -> bool:
        """Inserts a node at a specific position."""
        if position < 0:
            return False

        if position == 0:
            new_node = ListNode(val, self.head)
            if self.head:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
            return True

        cur = self.head
        while cur and position - 1 > 0:
            cur = cur.next
            position -= 1

        if not cur:
            return False

        if cur == self.tail:
            new_node = ListNode(val, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
            return True

        temp = cur.next
        new_node = ListNode(val, temp, cur.prev)
        cur.next = new_node
        if temp:
            temp.prev = new_node
        return True

    def delete_by_value(self, key: T) -> bool:
        """Deletes the first occurrence of the node containing data."""
        cur = self.head
        while cur:
            if cur.val == key:
                if cur == self.head:
                    self.head = cur.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif cur == self.tail:
                    self.tail = cur.prev
                    self.tail.next = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def delete_at_position(self, position: int) -> bool:
        """Deletes a node at a specific index."""
        if position < 0 or not self.head:
            return False
        cur = self.head
        while cur and position > 0:
            cur = cur.next
            position -= 1
        if cur and position == 0:
            if not cur.prev:
                self.head = self.head.next
            else:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            return True
        return False

    def display(self) -> None:
        """Traverses from the start to end."""
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def search(self, key: T) -> bool:
        """Searches for key in linked list."""
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

    def reverse(self) -> None:
        """Reverses the doubly linked list."""
        cur, prev = self.head, None
        while cur:
            cur.next, cur.prev, cur, prev = prev, cur.next, cur.next, cur
        self.head, self.tail = self.tail, self.head
