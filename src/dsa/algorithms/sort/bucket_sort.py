from src.dsa.algorithms.sort.sort_abc import Sort
from src.dsa.algorithms.sort.insertion_sort import InsertionSort

class BucketSort(Sort):
    def run(self, A: list[int], k = 0, algorithm=InsertionSort) -> list[int]:
        """ Performs bucket sorting on the provided Array of positive numbers.

        Args:
            A: Array to sort values >= 0
            k: number of buckets to create
            algorithm: sorting algorithm of choice

        Returns:
            res: after concatenating sorted buckets
        """
        if not A: return A
        if not k: k = len(A)
        buckets = [[] for _ in range(k)]
        max_value = max(A)
        for a in A:
            if a == max_value:
                buckets[-1].append(max_value)
            else:
                idx = (a * k) // max_value
                buckets[idx].append(a)
        res = []
        sorter = algorithm()

        for i in range(k):
            if buckets[i]:
                res.extend(sorter.run(buckets[i]))
        return res
