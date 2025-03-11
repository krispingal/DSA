import pytest

from src.dsa.algorithms.mathematic.prime_sieve import eratosthenes_sieve


class TestPrimeSieve:

    @pytest.mark.parametrize(
        "actual, expected, msg",
        [
            (1, [], "1 is not a prime"),
            (2, [2], "2 is a prime"),
            (20, [2, 3, 5, 7, 11, 13, 17, 19], "Primes till 20"),
        ],
    )
    def test_sieve_of_eratosthenes(self, actual, expected, msg):
        assert eratosthenes_sieve(actual) == expected, msg

    @pytest.mark.parametrize(
        "actual, expected_length, msg",
        [(100, 25, "Primes till 20"), (1000, 168, "Primes till 1000")],
    )
    def test_sieve_of_eratosthenes_by_length(self, actual, expected_length, msg):
        assert len(eratosthenes_sieve(actual)) == expected_length, msg
