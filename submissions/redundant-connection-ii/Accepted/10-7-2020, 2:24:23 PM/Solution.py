// https://leetcode.com/problems/redundant-connection-ii

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        https://www.youtube.com/watch?v=lnmJT5b4NlM&t=565s
        """
        n = len(edges)
        parent = [0 for i in range(n + 1)] # parent in graph
        root = [i for i in range(n + 1)] # parent in union find set
        size = [1 for _ in range(n + 1)]
        
        def find(node):
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return root[node]
        
        ans1, ans2 = [], []
        
        # Step 1: Get parents for each node
        for edge in edges:
            u, v = edge[0], edge[1]
            if parent[v] > 0:
                ans1 = [parent[v], v]
                ans2 = edge
            parent[v] = u
                
        for edge in edges:
            if edge == ans2:
                continue
            u, v = edge[0], edge[1]
            pu, pv = find(u), find(v)
            if pu == pv:
                # case 2.2 and case 1
                return ans1 if len(ans1) > 0 else edge
            if size[pu] > size[pv]:
                pu, pv = pv, pu
            root[pu] = pv
            size[pv] += size[pu]
            
        return ans2 # case 2.1