""""Implements prime sieves."""
class Solution:
    def eratosthenes_sieve(self, n: int) -> list[int]:
        """" Performs Eratosthenes sieve to generate a list of prime numbers till n

        Parameters
        ----------
        n: Inclusive limit till the sieve is computed against

        Returns
        -------
        res - list of primes till n

        """
        A = [1] * (n - 1)
        res = []
        for i in range(2, n+1):
            if A[i - 2]:
                res.append(i)
                for j in range(i*i, n+1, i):
                    A[j - 2] = 0
        return res

