// https://leetcode.com/problems/largest-1-bordered-square

class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        dp = [[[0] * 2 for _ in range(col + 1)] for _ in range(row + 1)]
        # dp[i][j][0]: concecutive 1 from down to top
        # dp[i][j][1]: 
        
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                if grid[r-1][c-1]:
                    dp[r][c][0] = dp[r-1][c][0] + 1
                    dp[r][c][1] = dp[r][c-1][1] + 1
                    
        ans = 0
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                if grid[r-1][c-1]:
                    p1 = min(dp[r][c])
                    for k in range(p1, 0, -1):
                        p2 = min(dp[r-k+1][c][1], dp[r][c-k+1][0])
                        if p2 >= k:
                            ans = max(ans, k * k)
                            break
                        
        return ans