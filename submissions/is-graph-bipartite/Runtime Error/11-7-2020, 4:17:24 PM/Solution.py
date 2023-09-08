// https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        queue = collections.deque()
        n = len(graph)
        neighs = collections.defaultdict(list)
        colors = collections.defaultdict(int)
        for i in range(n):
            for j in graph[i]:
                neighs[i].append(j)
        
        start = list(neighs.keys())[0]
        queue.append((start, 0))
        while queue:
            node, color = queue.popleft()
            if node in colors:
                if colors[node] != color:
                    return False
                continue
            colors[node] = color
            for nei in neighs[node]:
                queue.append((nei, abs(color - 1)))
                
        return True