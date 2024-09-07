"""Implementation of insertion sort."""
from random import sample
from timeit import timeit
from src.dsa.algorithms.sort.sort_abc import Sort


class InsertionSort(Sort):
    def run(self, A: list[int]) -> list[int]:
        for i in range(1, len(A)):
            x , j = A[i], i - 1
            while j >= 0 and A[j] > x:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = x
        return A

if __name__ == '__main__':
    T1 = [5, 4, 2, 3, 1]
    T2 = [2]
    T3 = []
    insort = InsertionSort()
    assert insort.run(T1) == [1, 2, 3, 4, 5]
    assert insort.run(T2) == [2]
    assert insort.run(T3) == []
    SZ = 1000
    unsorted = sample(range(-500, 500), SZ)
    NUM_RUNS = 1000
    timer = timeit("insort.run(unsorted)", globals=globals(), number=NUM_RUNS)
    print(f'Insertion sort completion time for array size: {SZ} {timer / NUM_RUNS:.5f}s')