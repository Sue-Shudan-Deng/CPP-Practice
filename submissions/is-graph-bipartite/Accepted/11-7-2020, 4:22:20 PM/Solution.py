// https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if graph == [[]]:
            return True
        queue = collections.deque()
        n = len(graph)
        colors = collections.defaultdict(int)
        
        for i in range(n):
            if i in colors or not graph[i]:
                continue
            queue.append((i, 0))
            while queue:
                node, color = queue.popleft()
                if node in colors:
                    if colors[node] != color:
                        return False
                    continue
                colors[node] = color
                for nei in graph[node]:
                    queue.append((nei, abs(color - 1)))
                
        return True