// https://leetcode.com/problems/unique-paths-iii

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        method 1: backtrack
        https://www.youtube.com/watch?v=dSXtmaGr4Fc method 1
        """
        row, col, cnt = len(grid), len(grid[0]), 1
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                elif grid[r][c] == 0:
                    cnt += 1
        
        def backtrack(r, c, n):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == -1:
                return 0
            if (r, c) == end:
                return n == 0
            # set
            grid[r][c] = -1
            # backtrack
            paths = backtrack(r - 1, c, n - 1) + \
                    backtrack(r + 1, c, n - 1) + \
                    backtrack(r, c - 1, n - 1) + \
                    backtrack(r, c + 1, n - 1)
            # reset
            grid[r][c] = 0
            return paths
        
        return backtrack(start[0], start[1], cnt)
        
        """
        method 2: TSP + DP
        https://www.youtube.com/watch?v=dSXtmaGr4Fc method 2
        """
    
    
    
    