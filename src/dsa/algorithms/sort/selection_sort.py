""""Implementation of Selection sort """

from src.dsa.algorithms.sort.sort_abc import Sort

class SelectionSort(Sort):
    def run(self, A: list[int]) -> list[int]:
        for i in range(len(A) - 1):
            min_idx = i
            for j in range(i + 1, len(A)):
                if A[min_idx] > A[j]:
                    min_idx = j
            A[min_idx], A[i] = A[i], A[min_idx]
        return A
