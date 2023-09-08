// https://leetcode.com/problems/find-the-shortest-superstring

class Solution:
    def __init__(self):
        self.best_path = []
    
    def shortestSuperstring(self, A: List[str]) -> str:
        """
        method 1: 当成一道常规的dfs + search问题来做
        """
#         n = len(A)
#         cost = [[0 for _ in range(n)] for _ in range(n)]
#         # cost[i][j] represents number of letters needed of appending A[j] to A[i] 
#         for i in range(n):
#             for j in range(n):
#                 cost[i][j] = len(A[j])
#                 for k in range(1, min(len(A[i]), len(A[j])) + 1):
#                     if A[i][-k:] == A[j][:k]:
#                         cost[i][j] = len(A[j]) - k
                
#         best_len = sum([len(n) for n in A])
#         def dfs(depth, used, cur_len, cur_path):
#             nonlocal best_len
#             if cur_len > best_len:
#                 return
#             if depth == n:
#                 best_len = cur_len
#                 self.best_path = cur_path
#                 return
#             for i in range(n):
#                 if used & (1 << i):
#                     continue
#                 dfs(depth + 1,
#                     used | (1 << i),
#                     cur_len + cost[cur_path[-1]][i]
#                     if depth else len(A[i]),
#                     cur_path + [i]
#                    )
                
#         dfs(0, 0, 0, [])
#         res = A[self.best_path[0]]
#         for i in range(1, n):
#             last = self.best_path[i-1]
#             cur = self.best_path[i]
#             res += A[cur][len(A[cur])-cost[last][cur]:]
#         return res
        """
        method 2: DP (TSP), https://www.youtube.com/watch?v=u_Wc4jwrp3Q
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
                        
        dp = [[float("inf") for _ in range(n)] for _ in range(1<<n)]
        parent = [[-1 for _ in range(n)] for _ in range(1<<n)]
        # child[s][i] = j: child of i is j
        
        for i in range(n):
            dp[1<<i][i] = len(A[i])
        for s in range(1, 1<<n):
            for i in range(n):
                if not s & (1<<i):
                    continue
                for j in range(n):
                    if dp[s-(1<<i)][j] + cost[j][i] < dp[s][i]:
                        dp[s][i] = dp[s-(1<<i)][j] + cost[j][i]
                        parent[s][i] = j
                        
        cur = [k for (k,v) in enumerate(dp[s]) if v == min(dp[s])][0]
        s, res = (1 << n) - 1, ""
        while s:
            pre = parent[s][cur]
            if pre < 0:
                res = A[cur] + res
            else:
                res = A[cur][-cost[pre][cur]:] + res
            s -= (1 << cur)
            cur = pre
        return res
        
                    
                    
                    
                    