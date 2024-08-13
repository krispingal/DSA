from random import sample
from timeit import timeit
from enum import Enum


class PartitionAlgorithm(Enum):
    LOMUTO = 1
    HOARE = 2


class QuickSort:
    def __init__(
            self,
            partition_algo: PartitionAlgorithm = PartitionAlgorithm.LOMUTO
            ) -> None:
        self.partition_algo = partition_algo

    def quicksort(self, A: list[int], lo: int, hi: int) -> None:
        if lo < hi:
            if self.partition_algo == PartitionAlgorithm.LOMUTO:
                p = self.lomuto_partition(A, lo, hi)
                self.quicksort(A, lo, p - 1)
                self.quicksort(A, p + 1, hi)
            elif self.partition_algo == PartitionAlgorithm.HOARE:
                p = self.hoare_partition(A, lo, hi)
                self.quicksort(A, lo, p)
                self.quicksort(A, p + 1, hi)

    def lomuto_partition(self, A: list[int], lo: int, hi: int) -> int:
        pivot = A[hi]
        i = lo
        for j in range(lo, hi):
            if A[j] <= pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[hi] = A[hi], A[i]
        return i

    def hoare_partition(self, A: list[int], lo: int, hi: int) -> int:
        pivot = A[lo]
        i, j = lo - 1, hi + 1
        while True:
            i += 1
            while A[i] < pivot:
                i += 1
            j -= 1
            while A[j] > pivot:
                j -= 1
            if i >= j: return j
            A[i], A[j] = A[j], A[i]


if __name__ == '__main__':
    partitionAlgorithm = PartitionAlgorithm.HOARE
    quickSort = QuickSort(partitionAlgorithm)
    T1 = [5, 4, 2, 3, 1]
    T2 = [5, 4, 2, 6, 3, 1]
    T3 = [2]
    T4 = []
    quickSort.quicksort(T1, 0, len(T1) - 1)
    assert T1 == [1, 2, 3, 4, 5]
    quickSort.quicksort(T2, 0, len(T2) - 1)
    assert T2 == [1, 2, 3, 4, 5, 6]
    quickSort.quicksort(T3, 0, len(T3) - 1) 
    assert T3 == [2]
    quickSort.quicksort(T4, 0, len(T4) - 1)
    assert T4 == []
    SZ = 200
    unsorted = sample(range(-100, 100), SZ)
    NUM_RUNS = 1000
    timer = timeit("quickSort.quicksort(unsorted, 0, SZ-1)", globals=globals(), number=NUM_RUNS)
    print(f'Quick sort {partitionAlgorithm} partition algo completion time for array size: {SZ} {timer/NUM_RUNS:.5f}s')