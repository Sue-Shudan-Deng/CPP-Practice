// https://leetcode.com/problems/number-of-islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # method 1: BFS
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] == '0'
                    queue = collections.deque([(i, j)])
                    while queue:
                        r, c = queue.popleft()
                        grid[r][c] = '0'
                        for d in directs:
                            new_r, new_c = r + d[0], c + d[1]
                            if new_r >= 0 and new_r <= row - 1 and new_c >= 0 and new_c <= col - 1 and grid[new_r][new_c] == '1':
                                queue.append((new_r, new_c))
        return cnt