// https://leetcode.com/problems/number-of-operations-to-make-network-connected

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        cnt = 0
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nonlocal cnt
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True
            
        cluster = set()
        for u, v in connections:
            if not union(u, v):
                cnt += 1
            
        for i in range(n):
            cluster.add(parent[i])
            
        if len(cluster) - 1 == cnt:
            return cnt
        else:
            return -1
            
        
            
        
        
            