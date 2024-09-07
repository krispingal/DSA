from random import sample
from timeit import timeit
from src.dsa.algorithms.sort.sort_abc import Sort
from src.dsa.datastructures.binary_tree_array import BinaryTree


class HeapSort(Sort):
    def __init__(self):
        self._tree = BinaryTree()

    def run(self, A: list[int]) -> list[int]:
        self.build_heap(A)
        n = len(A)
        for i in range(n - 1, 0, -1):
            self._tree.swap(0, i)
            self._max_heapify(0, i - 1)
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

if __name__ == '__main__':
    T1 = [5, 4, 2, 3, 1]
    T2 = [2]
    T3 = []
    heapsort = HeapSort()
    assert heapsort.run(T1) == [1, 2, 3, 4, 5]
    assert heapsort.run(T2) == [2]
    assert heapsort.run(T3) == []
    SZ = 10000
    unsorted = sample(range(-5000, 5000), SZ)
    NUM_RUNS = 50
    timer = timeit("heapsort.run(unsorted)", globals=globals(), number=NUM_RUNS)
    print(f'Heap sort completion time for array size: {SZ} {timer / NUM_RUNS:.5f}s')