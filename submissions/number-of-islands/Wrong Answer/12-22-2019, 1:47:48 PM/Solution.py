// https://leetcode.com/problems/number-of-islands

from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        nr = len(grid)
        if nr == 0:
            return 0       
        nc = len(grid[0])
        if nc == 0:
            return 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] == "0"
                    neighbors = deque()
                    neighbors.append((r, c))
                    while len(neighbors) > 0:
                        r, c = neighbors.popleft()
                        if r-1 >= 0 and grid[r-1][c] == "1":
                            neighbors.append((r-1, c))
                            grid[r-1][c] = "0"
                        if r+1 < nr and grid[r+1][c] == "1":
                            neighbors.append((r+1, c))
                            grid[r+1][c] = "0"
                        if c-1 >= 0 and grid[r][c-1] == "1":
                            neighbors.append((r, c-1))
                            grid[r][c-1] = "0"
                        if c+1 < nc and grid[r][c+1] == "1":
                            neighbors.append((r, c+1))
                            grid[r][c+1] = "0"
                            
        return num_islands