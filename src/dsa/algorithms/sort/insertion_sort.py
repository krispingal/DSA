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
