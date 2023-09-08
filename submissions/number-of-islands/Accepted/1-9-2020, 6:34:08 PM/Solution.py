// https://leetcode.com/problems/number-of-islands

# from collections import deque
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if grid == []:
#             return 0
#         row = len(grid)
#         column = len(grid[0])
#         queue = deque()
#         directions = [(0,1), (0,-1), (1,0), (-1,0)]
#         count = 0
        
#         for r in range(row):
#             for c in range(column):
#                 if grid[r][c] == "1":
#                     grid[r][c] = "0"
#                     count += 1   
#                     queue = deque([(r,c)])
#                     while queue:
#                         r_base, c_base = queue.popleft()
#                         for d in range(len(directions)):
#                             new_r = r_base + directions[d][0]
#                             new_c = c_base + directions[d][1] 
#                             if not (new_r < 0 or new_r >= row or new_c < 0 or new_c >= column \
#                             or grid[new_r][new_c] == "0"):
#                                 grid[new_r][new_c] = "0"
#                                 queue.append((new_r, new_c))
#         return count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(grid)
        col = len(grid[0])
        res = 0

        def dfs(r: int, c: int):
            grid[r][c] = "0"
            for d in range(len(directions)):
                new_r = r + directions[d][0]
                new_c = c + directions[d][1]
                if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col or grid[new_r][new_c] == "0":
                    continue
                dfs(new_r, new_c)
                
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        
        return res