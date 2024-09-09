import pytest

from src.dsa.algorithms.sort.bubble_sort import BubbleSort
from src.dsa.algorithms.sort.insertion_sort import InsertionSort
from src.dsa.algorithms.sort.heap_sort import HeapSort

class TestSortAlgorithms:
    @pytest.mark.parametrize("sort_class", [
        BubbleSort, InsertionSort, HeapSort
    ])
    def test_sorting_algorithms(self, sort_class):
        sorter = sort_class()
        assert sorter.run([3, 1, 2]) == [1, 2, 3]
        assert sorter.run([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert sorter.run([1]) == [1]
        assert sorter.run([]) == []
        assert sorter.run([10, -1, 0, 7, 3]) == [-1, 0, 3, 7, 10]
