from random import sample
from timeit import timeit

""" Bubble Sort
    Bubble sort is algorithm to sort a list/array of numbers
    by comparing an element with its succeding neighbor. When 
    it compares and sees a pair in which the succeeding element 
    is lesser than the preceeding element, the numbers gets 
    swapped.

    Time complexity: O(n) - where n is the number of elements
    Space complexity: O(1) 
"""
class BubbleSort():
    def run(self, A: list[int]) -> list[int]:
        n = len(A)
        for i in range(n-1):
            for j in range(i+1, n):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        return A


if __name__ == "__main__":
    T1 = [5, 4, 2, 3, 1]
    T2 = [2]
    T3 = []
    bub = BubbleSort()
    assert bub.run(T1) == [1, 2, 3, 4, 5]
    assert bub.run(T2) == [2]
    assert bub.run(T3) == []
    SZ = 1000
    unsorted = sample(range(-500, 500), SZ)
    NUM_RUNS = 1000
    timer = timeit("bub.run(unsorted)", globals=globals(), number=NUM_RUNS)
    print(f'Bubble sort completion time for array size: {SZ} {timer/NUM_RUNS:.5f}s')
