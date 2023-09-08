// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        dp[k][i] = triangle[k][i] + min(dp[k+1][i], dp[k+1][i+1])
        """
        n = len(triangle)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[-1] = triangle[-1]
        for k in range(n - 2, -1, -1):
            for i in range(k + 1):
                dp[k][i] = triangle[k][i] + min(dp[k+1][i], dp[k+1][i+1])
        return dp[0][0]