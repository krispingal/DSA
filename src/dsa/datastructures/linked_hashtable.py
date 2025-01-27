import math
from src.dsa.datastructures.doubly_linked_list import DoublyLinkedList
from src.dsa.datastructures.dictionary_abc import Dictionary


def div_hash(k: int, m: int) -> int:
    return k % m


def multiplication_hash(k: int, m: int, A: float = 0.61803398875) -> int:
    return math.floor(m * ((k * A) % 1))


class LinkedHashTable(Dictionary):
    _SENTINEL = object()

    def __init__(self, size=23, hash_function=div_hash):
        self._size = size
        self._hashtable = [self._SENTINEL] * self._size
        self._hash_function = hash_function
        self._count = 0

    def _hash(self, key) -> int:
        return self._hash_function(key, self._size)

    def _validate_index(self, idx) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of bounds")

    def _resize(self):
        old_hashtable = self._hashtable
        self._size *= 2  # Double the capacity
        self._hashtable = [self._SENTINEL] * self._size
        self._count = 0

        for dll in old_hashtable:
            if dll is not None:
                for node in dll:  # Reinsert elements into the new hashtable
                    self.put(node.val[0], node.val[1])

    def get(self, key, default=None):
        idx = self._hash(key)
        self._validate_index(idx)
        dll = self._hashtable[idx]
        if dll == self._SENTINEL:
            return default
        for node in dll:
            if node.val[0] == key:
                return node.val[1]
        return default

    def put(self, key, value):
        idx = self._hash(key)
        self._validate_index(idx)
        if self._hashtable[idx] == self._SENTINEL:
            self._hashtable[idx] = DoublyLinkedList()
        dll = self._hashtable[idx]
        for node in dll:
            if node.val[0] == key:
                node.val = (key, value)
                return

        dll.append((key, value))
        self._count += 1

        # Resize if load factor exceeds 0.75
        if self._count / self._size > 0.75:
            self._resize()

    def delete(self, key):
        idx = self._hash(key)
        self._validate_index(idx)
        dll = self._hashtable[idx]
        if dll == self._SENTINEL:
            raise KeyError(f"Key {key} not found")
        for node in dll:
            if node.val[0] == key:
                dll.delete_by_value(node.val)
                self._count -= 1
                return
        raise KeyError(f"Key {key} not found")

    def contains(self, key):
        """Check if key exists in dictionary."""
        idx = self._hash(key)
        self._validate_index(idx)
        dll = self._hashtable[idx]
        if dll == self._SENTINEL:
            return False
        for node in dll:
            if node.val[0] == key:
                return True
        return False

    def __iter__(self):
        for dll in self._hashtable:
            if dll is not None:
                for node in dll:
                    yield node.val

    def __len__(self):
        return self._count
