""""Implements prime sieves."""
import math
class Solution:
    def eratosthenes_sieve(self, n: int) -> list[int]:
        """" Performs Eratosthenes sieve to generate a list of prime numbers till n

        Parameters
        ----------
        n: Inclusive limit till the sieve is computed against

        Returns
        -------

        """
        A = [1] * (n - 1)
        res = []
        for i in range(2, n+1):
            if A[i - 2]:
                res.append(i)
                for j in range(i*i, n+1, i):
                    A[j - 2] = 0
        return res

if __name__ == '__main__':
    sol = Solution()
    assert len(sol.eratosthenes_sieve(1000)) == 168
