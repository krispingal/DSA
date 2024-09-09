from src.dsa.datastructures.binary_tree_array import BinaryTree
from src.dsa.algorithms.sort.sort_abc import Sort


class HeapSort(Sort):
    def __init__(self):
        self._tree = BinaryTree()

    def run(self, A: list[int]) -> list[int]:
        self.build_heap(A)
        n = len(A)
        for i in range(n - 1, 0, -1):
            self._tree.swap(0, i)
            self._max_heapify(0, i)
        return self._tree._arr

    def _max_heapify(self, i: int, l) -> None:
        if i >= l: return
        largest, left, right = i, self._tree.left_idx(i), self._tree.right_idx(i)
        if left < l and self._tree[left] > self._tree[i]:
            largest = left
        if right < l and self._tree[right] > self._tree[largest]:
            largest = right
        if largest != i:
            self._tree.swap(largest, i)
            self._max_heapify(largest, l)

    def build_heap(self, A: list) -> None:
        self._tree = BinaryTree(A)
        for i in range(len(A) // 2 - 1, -1, -1):
            self._max_heapify(i, len(A))
