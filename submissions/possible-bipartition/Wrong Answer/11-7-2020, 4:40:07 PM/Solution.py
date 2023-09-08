// https://leetcode.com/problems/possible-bipartition

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colors = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, N + 1):
            if i in colors:
                continue
            queue = collections.deque()
            queue.append((i, 0))
            while queue:
                n, color = queue.popleft()
                colors[n] = color
                if n in colors:
                    if colors[n] != color:
                        return False
                    continue
                for nei in graph[i]:
                    queue.append((nei, abs(color - 1)))
            
        return True