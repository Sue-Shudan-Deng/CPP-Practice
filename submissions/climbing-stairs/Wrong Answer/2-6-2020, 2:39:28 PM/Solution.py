// https://leetcode.com/problems/climbing-stairs

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1,2]
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            for s in steps:
                dp[i] += dp[i-s]
        return dp[n]