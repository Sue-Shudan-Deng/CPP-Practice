// https://leetcode.com/problems/walls-and-gates

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gate = 0
        wall = -1
        inf = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        row = len(rooms)
        column = len(rooms[0])
        
        for r in range(row):
            for c in range(column):
                if rooms[r][c] == gate:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            for d in range(len(directions)):
                new_r = r + directions[d][0]
                new_c = c + directions[d][1]
                if new_r < 0 or new_r >= row or new_c < 0 or new_c >= column \
                or rooms[new_r][new_c] != inf:
                    continue
                queue.append((new_r, new_c))
                rooms[new_r][new_c] = rooms[r][c] + 1
        