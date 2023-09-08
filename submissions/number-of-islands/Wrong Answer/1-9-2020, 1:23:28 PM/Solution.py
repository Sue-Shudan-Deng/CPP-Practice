// https://leetcode.com/problems/number-of-islands

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        row = len(grid)
        column = len(grid[0])
        queue = deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == "1":
                    count += 1   
                    queue = deque([(r,c)])
                    while queue:
                        r, c = queue.popleft()
                        for d in range(len(directions)):
                            new_r = r + directions[d][0]
                            new_c = c + directions[d][1] 
                            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= column:
                                continue
                            if grid[new_r][new_c] == "1":
                                grid[new_r][new_c] = "0"
                                queue.append((new_r, new_c))
        return count