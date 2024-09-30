"""Implements various methods to find fibonacci numbers."""

from functools import cache


class Fibonacci:
    @cache
    def nth_fibonacci_recursive(self, n: int) -> int:
        """ " Finds the nth fibonacci number using
            top-down(memoization) dynamic programming approach.

        Args:
            n: The number

        Returns:
            nth fibonacci number

        """
        if n <= 1:
            return n
        return self.nth_fibonacci_recursive(n - 1) + self.nth_fibonacci_recursive(n - 2)

    def nth_fibonacci_iterative(self, n: int) -> int:
        """Finds the nth fibonacci number using
            bottom up dynamic programming approach.

        Args:
            n: The number

        Returns:
            nth fibonacci number

        """
        if n <= 1:
            return n
        prev, pprev = 0, 1
        for _ in range(n):
            prev, pprev = prev + pprev, prev
        return prev
