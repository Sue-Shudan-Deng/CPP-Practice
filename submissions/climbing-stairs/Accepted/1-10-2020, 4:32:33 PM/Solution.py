// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        for p in range(2, n+1):
            dp[p] = dp[p-1] + dp[p-2]
        return dp[n]