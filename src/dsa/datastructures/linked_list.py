"""Linked list implementation."""

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class ListNode(Generic[T]):
    """Represents a node in a Linked List.

    Each node contains a value and a reference to its next node.

    Attributes:
        val (T): The value stored in the node. Type is generic.
        next (Optional[ListNode]): Reference to the next node. Defaults to None.
    """

    def __init__(self, val: T, next: Optional["ListNode"] = None) -> None:
        """Initializes a ListNode.

        Args:
            val (T): The value to be stored in the node.
            next (Optional[ListNode], optional): Reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next


class LinkedList(Generic[T]):
    """Represents a linked list.

    This class provides the basic structure for a linked list, including methods
    to retrieve insert, update, delete, find, and retrieve elements.

    Attributes:
        head (Optional[ListNode]): The head node of the Linked List or None if the list is empty.
    """

    def __init__(self) -> None:
        """Initializes an empty linked list."""
        self.head = None

    def prepend(self, val: T) -> None:
        """Inserts a node at the beginning of the list.

        Args:
            val (T): The value to be inserted.

        Example:
            >>> linked_list = LinkedList[int]()
            >>> linked_list.prepend(10)
            >>> print(linked_list)
            10
        """
        new_node = ListNode(val, self.head)
        self.head = new_node

    def append(self, val: T) -> None:
        """Inserts a node at the end of the list.

        Args:
            val (T): The value to be inserted.

        Example:
            >>> linked_list = LinkedList[int]()
            >>> linked_list.append(20)
            >>> print(linked_list)
            20
        """
        if not self.head:
            self.head = ListNode(val, None)
            return
        cur = self.head
        # Traverse to the end of the list
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val, None)

    def insert_at_position(self, position: int, val: T) -> bool:
        """Inserts a node at a specific position.

        Args:
            position (int): The zero-based index where the value should be inserted.
            val (T): The value to be inserted.

        Returns:
            bool: ``True`` if the insertion succeeded, ``False`` otherwise.

        Example:
            >>> linked_list = LinkedList[int]()
            >>> linked_list.append(20)
            >>> linked_list.insert_at_position(0, 10)
            >>> print(linked_list)
            10 -> 20

        Notes:
            Returns ``False`` if the position is invalid (less than 0 or greater than the list length).
        """
        if position < 0:
            return False  # Negative positions are invalid.

        if position == 0:
            # Insert at the head of the list.
            new_node = ListNode(val, self.head)
            self.head = new_node
            return True

        cur = self.head
        index = 0
        while cur and index < position - 1:
            cur = cur.next
            index += 1

        if cur:
            # Insert at the given position.
            new_node = ListNode(val, cur.next)
            cur.next = new_node
            return True

        return False  # Position is beyond the list length.

    def delete_by_value(self, key: T) -> bool:
        """Deletes the first occurrence of the node containing the specified value.

        Args:
            key (T): The value to be deleted.

        Returns:
            bool: True if the deletion succeeded, False otherwise.

        Example:
            >>> linked_list = LinkedList[int]()
            >>> linked_list.append(20)
            >>> linked_list.delete_by_value(20)
            True

        Notes:
            Returns ``False`` if the value is not found in the list.
        """
        if self.head and self.head.val == key:
            # Handle deletion of the head node.
            self.head = self.head.next
            return True

        cur, prev = self.head, None
        while cur:
            if cur.val == key:
                # Link the previous node to the next node, effectively removing `cur`.
                if prev:
                    prev.next = cur.next
                return True
            prev, cur = cur, cur.next

        return False  # Value not found in the list.

    def delete_at_position(self, position: int) -> bool:
        """Deletes the node at the given position, if it exists.

        Args:
            position (int): The zero-based index of the node to delete.

        Returns:
            bool: True if the deletion succeeded, False otherwise.

        Example:
            >>> linked_list = LinkedList[int]()
            >>> linked_list.append(20)
            >>> linked_list.append(40)
            >>> linked_list.delete_at_position(0)
            True
            >>> print(linked_list)
            40

        Notes:
            Returns `False` if the position is invalid (less than 0 or greater than or equal to the list length).
        """
        if position < 0 or not self.head:
            return False

        cur, prev = self.head, None
        index = 0
        while cur and index < position:
            cur, prev = cur.next, cur
            index += 1

        if cur:
            if not prev:
                self.head = cur.next
            else:
                prev.next = cur.next
            return True

        return False

    def search(self, key: T) -> int:
        """Searches the list for the presence of a key.

        Args:
            key (T): The value to search for.

        Returns:
            int: The index of the first node containing the key, or -1 if not found.

        Example:
            >>> linked_list = LinkedList[str]()
            >>> linked_list.append("foo")
            >>> linked_list.append("bar")
            >>> linked_list.search("bar")
            1
            >>> linked_list.search("foobar")
            -1

        Notes:
            This operation has a time complexity of O(n), where n is the number of nodes in the list.
        """
        cur = self.head
        index = 0
        while cur:
            if cur.val == key:
                return index
            cur = cur.next
            index += 1
        return -1

    def get_node_at(self, index: int) -> Optional[ListNode]:
        """Returns the node at the given index.

        Args:
            index (int): The zero-based index of the node to retrieve.

        Returns:
            Optional[ListNode]: The node at the given index, or None if the index is invalid.

        Example:
            >>> linked_list = LinkedList[str]()
            >>> linked_list.append("foo")
            >>> linked_list.append("bar")
            >>> node = linked_list.get_node_at(1)
            >>> print(node.val if node else "Node not found")
            bar

        Notes:
            Returns `None` if the index is less than 0 or greater than or equal to the list length.
        """
        if index < 0:
            return None

        cur = self.head
        while cur and index > 0:
            index -= 1
            cur = cur.next

        return cur

    def reverse(self) -> None:
        """Reverses the order of the nodes in the linked list.

        Notes:
            After reversing, the head becomes the tail, and the tail becomes the head.

        Example:
            >>> linked_list = LinkedList[int]()
            >>> linked_list.append(10)
            >>> linked_list.append(20)
            >>> print(linked_list)  # 10 -> 20
            >>> linked_list.reverse()
            >>> print(linked_list)  # 20 -> 10
        """
        cur, prev = self.head, None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        self.head = prev

    def __str__(self) -> str:
        """Returns a string representation of the linked list.

        Example:
            >>> linked_list = LinkedList[int]()
            >>> linked_list.append(10)
            >>> linked_list.append(20)
            >>> print(linked_list)
            10 -> 20
        """
        values = []
        cur = self.head
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        return " -> ".join(values)
