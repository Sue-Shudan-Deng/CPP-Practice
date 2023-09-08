// https://leetcode.com/problems/evaluate-division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        这道题我的主要问题在于第一次想没有想到要用backtrack
        和robotcleaner类似，只要当前已经访问过的节点不能再次被访问(否则dfs将会成环，那么都需要思考backtrack)
        """
        graph = defaultdict(defaultdict)
        for i, (p, q) in enumerate(equations):
            graph[p][q] = values[i]
            graph[q][p] = 1.0 / values[i]
            
        def backtrack(cur, end, ans, visited):
            # set
            res = -1.0
            neis = graph[cur]
            visited.add(cur)
            for nei in neis:
                if nei in visited:
                    continue
                if nei == end:
                    return ans * graph[cur][nei]
                res = backtrack(nei, end, ans * graph[cur][nei], visited)
                if res != -1:
                    return res
            # clear
            visited.remove(cur)
            return -1
                
        res = []
        for begin, end in queries:
            if not begin in graph or not end in graph:
                res.append(-1.0)
            elif begin == end:
                res.append(1.0)
            else:
                visited = set()
                res.append(backtrack(begin, end, 1.0, visited))
        return res