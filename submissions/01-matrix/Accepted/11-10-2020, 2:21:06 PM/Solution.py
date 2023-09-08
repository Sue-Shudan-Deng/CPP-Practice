// https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        这里的方法是从0开始BFS
        """ 
        row = len(matrix)
        col = len(matrix[0])
        queue = collections.deque()
        dist = [[float("inf") for _ in range(col)] for _ in range(row)]  # 相当于初始化为 not visited
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                if not (new_r < 0 or new_r > row-1 or new_c < 0 or new_c > col-1):
                    if dist[new_r][new_c] > dist[r][c] + 1:  # unvisited
                        dist[new_r][new_c] = dist[r][c] + 1
                        queue.append((new_r, new_c))
                
        return dist
            