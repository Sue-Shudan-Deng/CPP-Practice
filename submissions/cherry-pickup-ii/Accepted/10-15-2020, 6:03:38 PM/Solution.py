// https://leetcode.com/problems/cherry-pickup-ii

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[[0 for _ in range(col)] for _ in range(col)] for _ in range(row)] 
        
        for r in range(row - 1, -1, -1):
            for c1 in range(col):
                for c2 in range(col):
                    tmp = grid[r][c1]
                    if c1 != c2:
                        tmp += grid[r][c2]
                    if r != row - 1:
                        tmp += max(dp[r+1][new_c1][new_c2] for new_c1 in                         [c1-1, c1, c1+1] for new_c2 in [c2-1, c2, c2+1] if 0 <=                           new_c1 < col and 0 <= new_c2 < col)
                    dp[r][c1][c2] = tmp
                    
        return dp[0][0][-1]