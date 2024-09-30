import pytest

from src.dsa.algorithms.math.fibonacci import Fibonacci


@pytest.fixture
def testcase():
    return []


class TestFibonacci:
    @pytest.mark.parametrize(
        "actual, expected, msg",
        [
            (0, 0, "0th fibonacci should return 0"),
            (2, 1, "2nd fibonacci should return 1"),
            (5, 5, "5th fibonacci should return 5"),
            (19, 4181, "19th fibonacci should return 4181"),
        ],
    )
    def test_fibonacci_recursive(self, actual, expected, msg):
        fib = Fibonacci()
        assert fib.nth_fibonacci_recursive(actual) == expected, msg

    @pytest.mark.parametrize(
        "actual, expected, msg",
        [
            (0, 0, "0th fibonacci should return 0"),
            (2, 1, "2nd fibonacci should return 1"),
            (5, 5, "5th fibonacci should return 5"),
            (19, 4181, "19th fibonacci should return 4181"),
        ],
    )
    def test_fibonacci_iterative(self, actual, expected, msg):
        fib = Fibonacci()
        assert fib.nth_fibonacci_iterative(actual) == expected, msg