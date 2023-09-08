// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        m = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            m[i][i] = arr[i]
            for j in range(i + 1, n):
                m[i][j] = max(m[i][j-1], arr[j])
        """
        method 1: recursion with mem
        """
#         dp = [[0 for _ in range(n)] for _ in range(n)]
#         def dfs(i, j):
#             if i == j:
#                 dp[i][j] = 0
#                 return 0
#             if dp[i][j]:
#                 return dp[i][j]
#             tmp = float("inf")
#             for k in range(i, j):
#                 tmp = min(tmp, dfs(i, k) + dfs(k+1, j) + maxarray[i][k] * maxarray[k+1][j])
#             dp[i][j] = tmp
#             return tmp
                
#         return dfs(0, len(arr) - 1)
        """
        method 2: DP
        """
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # 一定要注意到着来！！！
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = float("inf")
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + m[i][k] * m[k+1][j])
        return dp[0][n-1]