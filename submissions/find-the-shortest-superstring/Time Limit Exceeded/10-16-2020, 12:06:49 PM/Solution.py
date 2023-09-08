// https://leetcode.com/problems/find-the-shortest-superstring

class Solution:
    def __init__(self):
        self.best_path = []
    
    def shortestSuperstring(self, A: List[str]) -> str:
        """
        method 1: 当成一道常规的dfs + search问题来做
        """
        n = len(A)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        # cost[i][j] represents number of letters needed of appending A[j] to A[i] 
        for i in range(n):
            for j in range(n):
                cost[i][j] = len(A[j])
                for k in range(1, min(len(A[i]), len(A[j])) + 1):
                    if A[i][-k:] == A[j][:k]:
                        cost[i][j] = len(A[j]) - k
                
        best_len = sum([len(n) for n in A])
        def dfs(depth, used, cur_len, cur_path):
            nonlocal best_len
            if cur_len > best_len:
                return
            if depth == n:
                best_len = cur_len
                self.best_path = cur_path
                return
            for i in range(n):
                if used & (1 << i):
                    continue
                dfs(depth + 1,
                    used | (1 << i),
                    cur_len + cost[cur_path[-1]][i]
                    if cur_path != [] else len(A[i]),
                    cur_path + [i],
                   )
                
        dfs(0, 0, 0, [])
        res = A[self.best_path[0]]
        for i in range(1, n):
            last = self.best_path[i-1]
            cur = self.best_path[i]
            res += A[cur][len(A[cur])-cost[last][cur]:]
        return res