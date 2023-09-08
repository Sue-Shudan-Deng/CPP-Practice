// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = collections.deque()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    
        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < row and 0 <= nc < col:
                    yield nr, nc
        lvl = 0
        while queue:
            r, c, lvl = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, lvl + 1))
                    
        if any(1 in row for row in grid):
            return -1
        return lvl