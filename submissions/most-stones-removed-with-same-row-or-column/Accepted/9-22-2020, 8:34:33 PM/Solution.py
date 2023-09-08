// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(stones)
        for i in range(n):
            for j in range(i + 1, n):
                x = stones[i]
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        visited, ans = set(), 0
        
        def dfs(idx):
            visited.add(idx)
            for nei in graph[idx]:
                if not nei in visited: 
                    dfs(nei)
                    
        for i in range(n):
            if not i in visited:
                dfs(i)
                ans += 1
        return n - ans