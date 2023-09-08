// https://leetcode.com/problems/shortest-path-visiting-all-nodes

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n, queue = len(graph), collections.deque()
        ans, steps = 1 << n - 1, 0
        visited = [[0 for _ in range(n)] for _ in range(1 << n)]
        
        for i in range(n):
            queue.append((i, 1 << i))
            
        while queue:
            cur, visited_state = queue.popleft()
            if visited_state == ans:
                return steps + 1
            if visited_state in visited:
                continue
            for nei in graph[cur]:
                queue.append((nei, visited_state | (1 << nei)))
            steps += 1
            
        return -1