// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        row, col, heap = len(matrix), len(matrix[0]), []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r in range(row):
            for c in range(col):
                heapq.heappush(heap, (matrix[r][c], r, c))
                
        def dfs(r, c, step, visited):
            tmp = step
            visited.add((r, c))
            for dr, dc in dirs:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < row and 0 <= new_c < col and matrix[new_r][new_c] > matrix[r][c]:
                    new_step = dfs(new_r, new_c, step + 1, visited)
                    tmp = max(tmp, new_step)
            return tmp
                
        visited, ans = set(), 0
        while heap:
            val, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            ans = max(ans, dfs(r, c, 1, visited))
        return ans