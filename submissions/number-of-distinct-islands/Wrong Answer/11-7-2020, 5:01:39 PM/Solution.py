// https://leetcode.com/problems/number-of-distinct-islands

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        DFS + path signature
        """
        row = len(grid)
        col = len(grid[0])
        seen = set()
        
        def dfs(r, c, di = 0):
            if 0 <= r < row and 0 <= c < col and grid[r][c] and (r, c) not in seen:
                seen.add((r, c))
                shape.append(di)
                dfs(r - 1, c, 1)
                dfs(r + 1, c, 2)
                dfs(r, c - 1, 3)
                dfs(r, c + 1, 4)
        
        res = 0
        shapes = set()
        for r in range(row):
            for c in range(col):
                shape = []
                dfs(r, c)
                if shape:
                    if tuple(shape) not in shapes:
                        res += 1
                        shapes.add(tuple(shape))
        return res