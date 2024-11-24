"""Implements various methods to find fibonacci numbers.

If we denote F(n) as the nth fibonacci number, then
F(n) = F(n-1) + F(n-2)
and so on until F(1) = 1 and F(0) = 0
"""

from functools import cache


@cache
def nth_fibonacci_recursive(n: int) -> int:
    """Computes nth fibonacci number recursively.

    Finds the nth fibonacci number using top-down(memoization) dynamic programming approach.

    Args:
        n (int): The number >= 0

    Returns:
        nth fibonacci number

    """
    if n <= 1:
        return n
    return nth_fibonacci_recursive(n - 1) + nth_fibonacci_recursive(n - 2)


def nth_fibonacci_iterative(n: int) -> int:
    """Computes nth fibonacci number iteratively.

    Finds the nth fibonacci number using bottom up dynamic programming approach.

    Args:
        n (int): The number >= 0

    Returns:
        nth fibonacci number

    """
    if n <= 1:
        return n
    prev, pprev = 0, 1
    for _ in range(n):
        prev, pprev = prev + pprev, prev
    return prev
