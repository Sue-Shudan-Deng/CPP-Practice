// https://leetcode.com/problems/minimum-score-triangulation-of-polygon

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        """
        https://zxi.mytechroad.com/blog/leetcode/leetcode-weekly-contest-135-1037-1038-1039-1040/, 中间的图
        """
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])
        return dp[0][n-1]