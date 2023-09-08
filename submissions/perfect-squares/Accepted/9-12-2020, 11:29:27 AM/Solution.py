// https://leetcode.com/problems/perfect-squares

from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        """
        DP, build array [1, n], multiple sweeps
        """
        squares = [i**2 for i in range(0, int(math.sqrt(n) + 1))]
        print(squares)
        dp = [float("inf")] * (n + 1) 
        dp[0] = 0
        for i in range(1, n + 1):
            for s in squares:
                if i >= s:
                    dp[i] = min(dp[i], dp[i-s] + 1)
        return dp[-1]