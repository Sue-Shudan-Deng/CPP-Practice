// https://leetcode.com/problems/cut-off-trees-for-golf-event

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        row, col = len(forest), len(forest[0])
        f = [(r, c) for r in range(row) for c in range(col) if forest[r][c]]
        f.sort(key = lambda (r, c): forest[r][c])
        f = [(0, 0)] + f
        cnt = 0
        def neighbors(s):
            for nr, nc in ((s[0] + 1, s[1]), (s[0], s[1] + 1), (s[0] - 1, s[1]), (s[0], s[1] - 1)):
                if 0 <= nr < row and 0 <= nc < col and forest[nr][nc]:
                    yield (nr, nc)
        
        def bfs(s, t):
            seen, queue = set(s), collections.deque([(s, 0)])
            while queue:
                s, step = queue.popleft()
                if s == t:
                    return step
                for ns in neighbors(s):
                    if ns not in seen:
                        seen.add(ns)
                        queue.append((ns, step + 1))
            return float("-inf")
        
        for s, t in zip(f[:-1], f[1:]):
            cnt += bfs(s, t)
            if cnt == float("-inf"):
                return -1
        return cnt