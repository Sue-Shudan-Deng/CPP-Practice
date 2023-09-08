// https://leetcode.com/problems/jump-game-iv

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n, graph = len(arr), collections.defaultdict(set)
        for k, v in enumerate(arr):
            graph[v].add(k)
        dp = [0 for _ in range(n)]
        
        def dfs(i, step, visited):
            if i == n - 1:
                return step
            tmp = float("inf")
            visited.add(i)
            # add 1
            if i + 1 < n and not i + 1 in visited:
                tmp = min(tmp, dfs(i + 1, step + 1, visited))
            # minus 1
            if i - 1 >= 0 and not i - 1 in visited:
                tmp = min(tmp, dfs(i - 1, step + 1, visited))
            # go to graph
            for j in graph[arr[i]]:
                if j != i + 1 and j != i - 1 and not j in visited:
                    tmp = min(tmp, dfs(j, step + 1, visited))
            visited.remove(i)
            return tmp
        
        return dfs(0, 0, set())