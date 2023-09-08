// https://leetcode.com/problems/cut-off-trees-for-golf-event

class Solution(object):
    def cutOffTree(self, f):
        row, col = len(f), len(f[0])
        s = [(i,j) for i in range(row) for j in range(col) if f[i][j]]             
        s.sort(key = lambda x: f[x[0]][x[1]])
        s = [(0,0)] + s
        cnt = 0
        
        def bfs(source, target):
            queue = collections.deque([(source,0)])
            visited = set()
            while queue:
                u, steps = queue.popleft()
                if u in visited:
                    continue
                visited.add(u)
                if u == target:
                    return steps
                r, c = u[0], u[1]
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < row and 0 <= nc < col and f[nr][nc]:
                        queue.append((v, steps + 1))
            return float('inf')
        
        for u, v in zip(s, s[1:]): 
            cnt += bfs(u, v)
            if cnt == float('inf'): 
                return -1
        return cnt
    
