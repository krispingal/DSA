"""Binary tree implemented using an array."""
from dataclasses import dataclass, field
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class BinaryTree(Generic[T]):
    _arr: list[T] = field(default_factory=list)

    @property
    def root(self):
        return self._arr[0]

    def insert(self, v: T) -> None:
        self._arr.append(v)

    def parent_idx(self, i: int) -> int:
        """Gets the parent index of `i`."""
        return (i - 1) // 2

    def left_idx(self, i: int) -> int:
        """Gets the index of the left child of `i`."""
        return 2 * i + 1

    def right_idx(self, i: int) -> int:
        """Gets the index of the right child of `i`."""
        return 2 * i + 2

    def pop(self) -> int:
        """Pops last element from binary tree array."""
        return self._arr.pop()

    def swap(self, i: int, j: int) -> None:
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]

    def set(self, i: int, v: T) -> None:
        self._arr[i] = v

    def __len__(self):
        return len(self._arr)

    def __getitem__(self, k: int):
        return self._arr[k]

if __name__ == '__main__':
    btree = BinaryTree()
    for i in range(10):
        btree.insert(i)
    print(btree)
    print(btree.left_idx(0))
    print(btree.right_idx(0))
    
    