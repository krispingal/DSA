from typing import Callable


class Solution:
    def bisect(self, A: list[int], target: int) -> int:
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def bisect_left(self, A: list[int], cond: Callable[[int], bool]) -> int:
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if cond(A[mid]):
                hi = mid
            else:
                lo = mid + 1
        return A[lo]

    def bisect_right(self, A: list[int], cond: Callable[[int], bool]) -> int:
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if cond(A[mid]):
                lo = mid
            else:
                hi = mid - 1
        return A[hi]


if __name__ == '__main__':
    sol = Solution()
    A = list(range(0, 300, 3))
    assert sol.bisect(A, 27) == 9
    assert sol.bisect(A, 25) == -1
    assert sol.bisect_left(A, lambda x: x > 100) == 102
    assert sol.bisect_left(A, lambda x: x > 500) == 297
    assert sol.bisect_right(A, lambda x: x < 100) == 99
    assert sol.bisect_right(A, lambda x: x < -1) == 0
