from random import sample
from timeit import timeit


class Solution:
    def merge_sort(self, L: list[int]) -> list[int]:
        if len(L) < 2: return L
        mid = len(L) // 2
        L1 = self.merge_sort(L[:mid])
        L2 = self.merge_sort(L[mid:])
        return self.merge(L1, L2, L)
    
    def merge(self, L1: list[int], L2: list[int], L: list[int]):
        i = j = 0
        while i + j < len(L):
            if j == len(L2) or (i < len(L1) and L1[i] < L2[j]):
                L[i+j] = L1[i]
                i += 1
            else:
                L[i+j] = L2[j]
                j += 1
        return L


if __name__ == '__main__':
    sol = Solution()
    T1 = [5, 4, 2, 3, 1]
    T2 = [2]
    T3 = []
    print(sol.merge_sort(T1))
    assert sol.merge_sort(T1) == [1, 2, 3, 4, 5]
    assert sol.merge_sort(T2) == [2]
    assert sol.merge_sort(T3) == []
    SZ = 1000
    unsorted = sample(range(-500, 500), SZ)
    NUM_RUNS = 1000
    timer = timeit("sol.merge_sort(unsorted)", globals=globals(), number=NUM_RUNS)
    print(f'Merge sort completion time for array size: {SZ} {timer/NUM_RUNS:.5f}s')
    