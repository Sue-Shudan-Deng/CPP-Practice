// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if grid[0][0] != 2:
            return 0
        queue = collections.deque()
        queue.append((0, 0, 0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        lvl = 0
        
        while queue:
            r, c, lvl = queue.popleft()
            grid[r][c] = 2
            for d_r, d_c in dirs:
                new_r = d_r + r
                new_c = d_c + c
                if new_r >= 0 and new_r < row and new_c >= 0 and new_c < col and grid[new_r][new_c] == 1:
                    queue.append((new_r, new_c, lvl + 1))
                    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
                
        return lvl