// https://leetcode.com/problems/trapping-rain-water-ii

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        priority_queue = []
        row, col = len(heightMap), len(heightMap[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = [[0 for _ in range(col)] for _ in range(row)]
        ans = 0
        if row <= 2 or col <= 2:
            return 0
        
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    priority_queue.append((heightMap[i][j], i, j))
                    visited[i][j] = 1
            
        heapq.heapify(priority_queue)
        while priority_queue:
            val, r, c = heapq.heappop(priority_queue)
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < row and 0 <= new_c < col and not visited[new_r][new_c]:
                    ans += max(0, heightMap[r][c] - heightMap[new_r][new_c])
                    heightMap[new_r][new_c] = max(heightMap[r][c], heightMap[new_r][new_c])
                    heapq.heappush(priority_queue, (heightMap[new_r][new_c], new_r, new_c))
                    visited[new_r][new_c] = 1
        return ans  