// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == []:
            return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(0, row):
            for j in range(0, col):
                if i == 0 and j == 0:
                    tmp = 0
                elif i-1 < 0:
                    tmp = dp[i][j-1]
                elif j-1 < 0:
                    tmp = dp[i-1][j]
                else:
                    tmp = min(dp[i-1][j], dp[i][j-1])
                dp[i][j] = grid[i][j] + tmp
        return dp[-1][-1]