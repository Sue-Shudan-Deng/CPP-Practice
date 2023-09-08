// https://leetcode.com/problems/jump-game-iv

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        method 1: DFS, O(n), TLE
        """
#         n, graph = len(arr), collections.defaultdict(set)
#         for k, v in enumerate(arr):
#             graph[v].add(k)
#         dp = [0 for _ in range(n)]
        
#         def dfs(i, step, visited):
#             if i == n - 1:
#                 return step
#             tmp = float("inf")
#             visited.add(i)
#             # add 1
#             if i + 1 < n and not i + 1 in visited:
#                 tmp = min(tmp, dfs(i + 1, step + 1, visited))
#             # minus 1
#             if i - 1 >= 0 and not i - 1 in visited:
#                 tmp = min(tmp, dfs(i - 1, step + 1, visited))
#             # go to graph
#             for j in graph[arr[i]]:
#                 if j != i + 1 and j != i - 1 and not j in visited:
#                     tmp = min(tmp, dfs(j, step + 1, visited))
#             visited.remove(i)
#             return tmp
        
#         return dfs(0, 0, set())
        """
        method 2: BFS，而且更令人吃惊的是，这里甚至不需要对每个branch单独存visited
        """
        n, graph = len(arr), collections.defaultdict(set)
        for k, v in enumerate(arr):
            graph[v].add(k)
            
        queue, ans = collections.deque(), 0
        queue.append((0, 0))
        visited = [0 for _ in range(n)]
        visited[0] = 1
        
        while queue:
            i, step = queue.popleft()
            if i == n - 1:
                return step
            # add 1
            if i + 1 < n and not visited[i + 1]:
                queue.append((i + 1, step + 1))
                visited[i + 1] = 1
            # minus 1
            if i - 1 >= 0 and not visited[i - 1]:
                queue.append((i - 1, step + 1))
                visited[i - 1] = 1
            # go to graph
            for j in graph[arr[i]]:
                if j != i + 1 and j != i - 1 and not visited[j]:
                    queue.append((j, step + 1))
                    visited[j] = 1
            # 优化， 见https://www.youtube.com/watch?v=SsAfFd9aN8I
            del graph[arr[i]] # 主要是为了防止55行被重复访问浪费时间
        
        return -1