"""Compute maximum sub array sum of a given array."""

class Solution:
    def max_sub_arr(self, A: list[int]) -> int:
        """Performs Kadane's algorithm to find the maximum sub array sum.
            Time Complexity: O(T) : O(n) - n is # of elem in array
            Space complexity: O(S) : O(1)
            Parameters
            ----------
            A: list[int] - the array

            Returns
            -------
            maxSum - the maximum sub array sum value

        """
        curSum = maxSum = A[0]
        for a in A[1:]:
            curSum = max(curSum + a, a)
            maxSum = max(maxSum, curSum)
        return maxSum

if __name__ == '__main__':
    sol = Solution()
    assert sol.max_sub_arr([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sol.max_sub_arr([5,4,-1,7,8]) == 23
