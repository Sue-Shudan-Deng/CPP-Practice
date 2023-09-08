// https://leetcode.com/problems/find-eventual-safe-states

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visiting, visited = set(), set()
        unsafe = []
        
        def dfs(node, cur):
            if node in visited:
                return []
            if node in visiting:
                unsafe = cur[:]
                return unsafe
            
            visiting.add(node)
            for nei in graph[node]:
                res = dfs(nei, cur + [nei])
                if res:
                    return res
            visiting.remove(node)
            visited.add(node)
            return []
            
        res = []
        for i in range(n):
            unsafe = dfs(i, [i])
            for i in unsafe:
                visited.add(i)
            res += unsafe
                
        return [i for i in range(n) if not i in res]