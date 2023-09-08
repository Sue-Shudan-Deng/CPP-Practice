// https://leetcode.com/problems/number-of-islands-ii

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        parent = [-1 for _ in range(m * n)]
        size = [0 for _ in range(m * n)]
        cnt = 0
        ans = []
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]
        
        def union(x, y):
            nonlocal cnt
            px, py = find(x), find(y)
            if px == py:
                return
            if size[px] > size[py]:
                px, py = py, px
            parent[px] = py
            size[py] += size[px]
            cnt -= 1
            
        for r, c in positions:
            if r - 1 >= 0 and parent[(r - 1) * n + c] >= 0:
                union(r * n + c, (r - 1) * n + c)
            if c - 1 >= 0 and parent[r * n + (c - 1)] >= 0:
                union(r * n + c, r * n + (c - 1))
            if r + 1 < m and parent[(r + 1) * n + c] >= 0:
                union(r * n + c, (r + 1) * n + c)
            if c + 1 < n and parent[r * n + (c + 1)] >= 0:
                union(r * n + c, r * n + (c + 1))
            
            parent[r * n + c] = r * n + c
            cnt += 1
            ans.append(cnt)
            
        return ans
            
                
            