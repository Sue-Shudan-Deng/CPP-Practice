// https://leetcode.com/problems/critical-connections-in-a-network

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        g = collections.defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)
        
        jump = [-1] * n
        
        def dfs(v: int, par: int, lvl: int, res: list, jump: list, g) -> int:
            
            jump[v] = lvl + 1
            for child in g[v]:
                if child == par:
                    pass
                elif jump[v] == -1:
                    jump[v] = min(jump[v], dfs(child, v, lvl + 1, res, jump, g))
                else:
                    jump[v] = min(jump[v], jump[child])
            if jump[v] == lvl + 1 and v != 0:
                res.append([par, v])
            return jump[v]
        
        res = []
        dfs(0, -1, 0, res, jump, g)
        return res