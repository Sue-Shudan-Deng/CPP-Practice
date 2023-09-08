// https://leetcode.com/problems/number-of-islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        
        def neighbors(r, c):
            for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1":
                    yield nr, nc
        
        seen = set()
        def dfs(r, c):
            if (r, c) in seen:
                return
            else:
                seen.add((r, c))
                for nr, nc in neighbors(r, c):
                    if (nr, nc) not in seen:
                        dfs(nr, nc)
        
        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    cnt += 1
        return cnt