// https://leetcode.com/problems/accounts-merge

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            n, name, root = len(acc), acc[0], acc[1]
            for i in range(1, n):
                graph[root].add(acc[i])
                graph[acc[i]].add(root)
                em_to_name[acc[i]] = name
                      
        visited, res = set(), []
        ans = 0
        
        def dfs(node, visited, ans):
            if node in visited:
                return
            visited.add(node)
            ans.append(node)
            for nei in graph[node]:
                dfs(nei, visited, ans)
            
        for node in graph:
            if not node in visited:
                ans = []
                dfs(node, visited, ans)
                res.append([em_to_name[node]] + sorted(ans))
                
        return res