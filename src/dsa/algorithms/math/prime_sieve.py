"""Implements prime sieves."""


def eratosthenes_sieve(n: int) -> list[int]:
    """
    Implements the Sieve of Eratosthenes algorithm to compute all prime numbers up to a given limit.

    This function efficiently generates a list of prime numbers by marking the multiples
    of each prime number starting from 2. It is a classic algorithm used in number theory.

    Args:
        n (int): The upper inclusive limit up to which primes are calculated. Must be a positive integer greater than 1.

    Returns:
        list[int]: A list of all prime numbers from 2 to `n`.

    Raises:
        ValueError: If `n` is less than 2, as the sieve cannot compute primes below this limit.

    Example:
        >>> primes = sieve_of_eratosthenes(10)
        >>> print(primes)
        [2, 3, 5, 7]

    References:
        - `Sieve of Eratosthenes on Wikipedia <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`_
        - `Sieve of Eratosthenes on YouTube - Khan Academy <https://www.youtube.com/watch?v=klcIklsWzrY>`_

    Notes:
        - **Performance**:
            - Time Complexity: O(n log log n), where `n` is the upper limit.
            - Space Complexity: O(n), for storing the sieve array.
        - This implementation uses a 0-based index internally for the sieve array.

    Warnings:
        - For very large values of `n`, the memory usage can be significant due to the array size.
    """
    A = [1] * (n - 1)
    res = []
    for i in range(2, n + 1):
        if A[i - 2]:
            res.append(i)
            for j in range(i * i, n + 1, i):
                A[j - 2] = 0
    return res
