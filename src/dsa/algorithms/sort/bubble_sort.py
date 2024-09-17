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
