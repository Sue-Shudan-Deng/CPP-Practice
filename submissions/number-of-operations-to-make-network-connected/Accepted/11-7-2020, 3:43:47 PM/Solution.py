// https://leetcode.com/problems/number-of-operations-to-make-network-connected

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        cnt = 0
        if len(connections) < n - 1:
            return -1
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
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
            cnt += 1
            
        cluster = set()
        for u, v in connections:
            union(u, v)
            
        for i in range(n):
            cluster.add(find(i))
            
        print(cluster)
        print(cnt)
        if len(cluster) == n - cnt:
            return n - cnt - 1
        else:
            return -1
            
        
            
        
        
            