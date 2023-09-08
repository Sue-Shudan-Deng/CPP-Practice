// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == []:
            return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[float("inf") for _ in range(col + 1)] for _ in range(row + 1)]
        dp[0][1], dp[1][0] = 0, 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]