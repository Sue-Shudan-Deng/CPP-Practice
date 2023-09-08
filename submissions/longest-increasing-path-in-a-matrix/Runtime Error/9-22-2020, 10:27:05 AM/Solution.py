// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col, heap = len(matrix), len(matrix[0]), []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r in range(row):
            for c in range(col):
                heapq.heappush(heap, (matrix[r][c], r, c))
                
        def dfs(r, c, step):
            tmp = step
            for dr, dc in dirs:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < row and 0 <= new_c < col and matrix[new_r][new_c] > matrix[r][c]:
                    new_step = dfs(new_r, new_c, step + 1)
                    tmp = max(tmp, new_step)
            return tmp
            
                
        ans = 0
        while heap:
            val, r, c = heapq.heappop(heap)
            x = dfs(r, c, 1)
            ans = max(ans, x)
        return ans