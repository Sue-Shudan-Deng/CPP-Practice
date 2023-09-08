// https://leetcode.com/problems/trapping-rain-water-ii

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        priority_queue = []
        row, col = len(heightMap), len(heightMap[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        ans = 0
        if row <= 2 or col <= 2:
            return 0
        
        for i in range(col):
            priority_queue.append((heightMap[0][i], 0, i))
            priority_queue.append((heightMap[row-1][i], row-1, i))
        for j in range(1, row-1):
            priority_queue.append((heightMap[j][0], j, 0))
            priority_queue.append((heightMap[j][col-1], j, col-1))
            
        heapq.heapify(priority_queue)
        while priority_queue:
            val, r, c = heapq.heappop(priority_queue)
            visited.add((r, c))
            for dr, dc in dirs:
                if r+dr >= 0 and r+dr < row and c+dc > 0 and c+dc < col and not (r+dr, c+dc) in visited:
                    ans += max(0, heightMap[r][c] - heightMap[r+dr][c+dc])
                    heightMap[r+dr][c+dc] = max(heightMap[r][c], heightMap[r+dr][c+dc])
                    heapq.heappush(priority_queue, (heightMap[r+dr][c+dc], r+dr, c+dc))
                    
        return ans
                    
                    