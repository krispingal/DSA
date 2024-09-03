"""Implementation of a priority queue using a max heap."""
import math

from src.dsa.datastructures.binary_tree_array import BinaryTree
from src.dsa.datastructures.max_priority_queue import MaxPriorityQueue


class MaxHeap(MaxPriorityQueue):
    def __init__(self):
        self._tree = BinaryTree()

    def get_max(self):
        self._tree.root

    def extract_max(self):
        if not len(self._tree): return IndexError
        self._tree.swap(0, -1)
        max = self._tree[-1]
        self._tree.pop()
        self._max_heapify(0)
        return max


    def _max_heapify(self, i: int) -> None:
        if i >= len(self._tree): return
        largest, left, right = i, self._tree.left_idx(i), self._tree.right_idx(i)
        if left < len(self._tree) and self._tree[left] > self._tree[i]:
            largest = left
        if right < len(self._tree) and self._tree[right] > self._tree[largest]:
            largest = right
        if largest != i:
            self._tree.swap(largest, i)
            self._max_heapify(largest)

    def insert(self, v) -> None:
        self._tree.insert(-math.inf)
        self.increase_key(len(self._tree)-1, v)


    def increase_key(self, i, k) -> None:
        if self._tree[i] > k: raise ValueError
        self._tree.set(i, k)
        while i > 0 and self._tree[self._tree.parent_idx(i)] < self._tree[i]:
            self._tree.swap(i, self._tree.parent_idx(i))
            i = self._tree.parent_idx(i)



    def build_heap(self, A: list) -> None:
        self._tree = BinaryTree(A)
        for i in range(len(A) // 2 - 1, -1, -1):
            self._max_heapify(i)

if __name__ == '__main__':
    heap =  MaxHeap()
    heap.build_heap([0,1,2,3,4,5,6])
    heap.insert(10)
    print(heap._tree)
    print(f'Max Element in max heap is {heap.extract_max()}')
    print(heap._tree)

