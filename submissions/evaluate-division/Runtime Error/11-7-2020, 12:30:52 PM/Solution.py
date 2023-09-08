// https://leetcode.com/problems/evaluate-division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        method 1: backtrack
        这道题我的主要问题在于第一次想没有想到要用backtrack
        和robotcleaner类似，只要当前已经访问过的节点不能再次被访问(否则dfs将会成环，那么都需要思考backtrack)
        """
        
        
        """
        method 2: union find
        """
        parent = collections.defaultdict(list)
        def find(x):
            """
            这个函数需要仔细理解
            """
            if x != parent[x][0]:
                p = find(parent[x][0])
                parent[x][0] = p[0]
                parent[x][1] *= p[1]
            return parent[x]
                
        for idx, (u, v) in enumerate(equations):
            k = values[idx] # u / v = k
            if not parent[u] and not parent[v]:
                # second node as parent
                parent[u] = [v, k]
                parent[v] = [v, 1.0]
            elif not parent[u]:
                # second node as parent
                parent[u] = [v, k]
            elif not parent[v]:
                # first node as parent
                parent[v] = [u, 1 / k]
            else:
                # second node as parent
                pu = parent[u]
                pv = parent[v]
                # u / pu = pu.second
                # v / pv = pv.second
                # u / v = k
                # pu / pv = 1 / pu.second * k * pv.second
                parent[pu] = [pv[0], 1 / pu[1] * k * pv[1]]
        
        ans = []
        for u, v in queries:
            if not parent[u] or not parent[v]:
                ans.append(-1.0)
                continue
            if u == v:
                ans.append(1.0)
                continue
            pu, pv = find(u), find(v)
            if pu[0] != pv[0]:
                # they don't even belong to the same cluster
                ans.append(-1.0)
            else:
                # pu.second = u / root
                # pv.second = v / root
                # u / v = pu.second / pv.second
                ans.append(pu[1] / pv[1])
        return ans
        
#         graph = defaultdict(defaultdict)
#         for i, (p, q) in enumerate(equations):
#             graph[p][q] = values[i]
#             graph[q][p] = 1.0 / values[i]
            
#         def backtrack(cur, end, ans, visited):
#             # set
#             res = -1.0
#             neis = graph[cur]
#             visited.add(cur)
#             for nei in neis:
#                 if nei in visited:
#                     continue
#                 if nei == end:
#                     return ans * graph[cur][nei]
#                 res = backtrack(nei, end, ans * graph[cur][nei], visited)
#                 if res != -1:
#                     return res
#             # clear
#             visited.remove(cur)
#             return -1
                
#         res = []
#         for begin, end in queries:
#             if not begin in graph or not end in graph:
#                 res.append(-1.0)
#             elif begin == end:
#                 res.append(1.0)
#             else:
#                 visited = set()
#                 res.append(backtrack(begin, end, 1.0, visited))
#         return res
    
    
    
    