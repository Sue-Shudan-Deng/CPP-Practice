// https://leetcode.com/problems/graph-valid-tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # topological sorting
        visited, visiting = set(), set()
        
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
            
        return True