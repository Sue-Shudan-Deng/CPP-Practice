// https://leetcode.com/problems/graph-valid-tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        684. Redundant Connection
        """
        parent = [i for i in range(n)]
        cnt = n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def Union(x, y):
            nonlocal cnt
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            cnt -= 1
            return True
            
        for u, v in edges:
            if not Union(u, v):
                return False
            
        return cnt == 1
        
        