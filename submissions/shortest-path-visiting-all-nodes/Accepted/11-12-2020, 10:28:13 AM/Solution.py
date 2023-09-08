// https://leetcode.com/problems/shortest-path-visiting-all-nodes

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n, queue = len(graph), collections.deque()
        ans, steps = (1 << n) - 1, 0
        visited = [[0 for _ in range(1 << n)] for _ in range(n)]
        
        for i in range(n):
            queue.append((i, 1 << i))
            
        while queue:
            s = len(queue)
            while s:
                s -= 1
                cur, state = queue.popleft()
                if state == ans:
                    return steps
                if visited[cur][state]:
                    continue
                visited[cur][state] = 1
                for nei in graph[cur]:
                    queue.append((nei, state | (1 << nei)))
            steps += 1
            
        return -1