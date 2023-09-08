// https://leetcode.com/problems/cut-off-trees-for-golf-event

class Solution(object):
    def cutOffTree(self, f):
        row, col = len(f), len(f[0])
        s = [(i,j) for i in range(row) for j in range(col) if f[i][j]]             
        s.sort(key = lambda x: f[x[0]][x[1]])
        s = [(0,0)] + s
        
        def bfs(source, target):
            queue = collections.deque([(source, 0)])
            visited = set()
            while queue:
                (r, c), steps = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                if (r, c) == target:
                    return steps
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < row and 0 <= nc < col and f[nr][nc]:
                        queue.append(((nr, nc), steps + 1))
            return float('inf')
        
        cnt = 0
        for u, v in zip(s, s[1:]): 
            res = bfs(u, v)
            cnt += res
            if cnt == float('inf'): 
                return -1
        return cnt
    
