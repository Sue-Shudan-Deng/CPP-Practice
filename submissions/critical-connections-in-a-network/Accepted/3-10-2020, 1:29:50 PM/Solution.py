// https://leetcode.com/problems/critical-connections-in-a-network

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        g = collections.defaultdict(set)
        for u, v in connections:
            g[u].add(v)
            g[v].add(u)
        
        # jump保留的是所在的clique(2个结点以上)中所有结点的最小值
        jump = [-1] * n
        
        def dfs(v: int, par: int, lvl: int, res: list, jump: list, g) -> int:
            
            jump[v] = lvl + 1
            
            for child in g[v]:
                # 如果child节点等于parent结点，继续
                if child == par:
                    continue
                # 如果child结点未被访问，则访问
                elif jump[child] == -1:
                    jump[v] = min(jump[v], dfs(child, v, lvl + 1, res, jump, g))
                # 如果child结点已经被访问过了，则直接返回
                else:
                    jump[v] = min(jump[v], jump[child])
            
            if jump[v] == lvl + 1 and v != 0:
                res.append([par, v])
            return jump[v]
        
        res = []
        dfs(0, -1, 0, res, jump, g)
        print(jump)
        return res