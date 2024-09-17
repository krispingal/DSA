import pytest

from src.dsa.algorithms.sort.bubble_sort import BubbleSort
from src.dsa.algorithms.sort.insertion_sort import InsertionSort
from src.dsa.algorithms.sort.heap_sort import HeapSort
from src.dsa.algorithms.sort.selection_sort import SelectionSort

class TestSortAlgorithms:
    @pytest.mark.parametrize("sort_class", [
        BubbleSort, InsertionSort, HeapSort, SelectionSort
    ])
    def test_sorting_algorithms(self, sort_class):
        sorter = sort_class()
        assert sorter.run([3, 1, 2]) == [1, 2, 3], "Sort should work with random numbers"
        assert sorter.run([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Sort should work with reverse sorted nums"
        assert sorter.run([1]) == [1], "Sort should run for single element array"
        assert sorter.run([]) == [], "Sort should run for empty element array"
        assert sorter.run([10, -1, 0, 7, 3]) == [-1, 0, 3, 7, 10], "Sort should run for arrays with negative elements."
