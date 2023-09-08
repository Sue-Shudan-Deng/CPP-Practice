// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == []:
            return 1
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
        
        if obstacleGrid[0][0] == 0:
            dp[1][1] = 1
        else:
            dp[1][1] = 0
        for i in range(1, row+1):
            for j in range(1, col+1):
                if not (i == 1 and j == 1) and obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]