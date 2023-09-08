// https://leetcode.com/problems/perfect-squares

from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        """
        Unbounded knapsack
        """
        candidates = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for num in candidates:
                if i >= num:
                    dp[i] = min(dp[i], dp[i - num] + 1)
        return dp[-1]