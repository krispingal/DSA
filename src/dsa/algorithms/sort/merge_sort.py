"""Implement Merge sort algorith,"""
class MergeSort:
    def merge_sort_recursive(self, L: list[int]) -> list[int]:
        """Implements merge sort algorithm recursively."""
        if len(L) < 2: return L
        mid = len(L) // 2
        L1 = self.merge_sort_recursive(L[:mid])
        L2 = self.merge_sort_recursive(L[mid:])
        return self._merge(L1, L2, L)
    
    def _merge(self, L1: list[int], L2: list[int], L: list[int]):
        i = j = 0
        while i + j < len(L):
            if j == len(L2) or (i < len(L1) and L1[i] < L2[j]):
                L[i+j] = L1[i]
                i += 1
            else:
                L[i+j] = L2[j]
                j += 1
        return L
