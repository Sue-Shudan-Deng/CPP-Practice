// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        maxarray = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                maxarray[i][j] = max(arr[i:j+1])
        def dfs(i, j):
            if i == j:
                dp[i][j] = 0
                return 0
            if dp[i][j]:
                return dp[i][j]
            tmp = float("inf")
            for k in range(i, j):
                tmp = min(tmp, dfs(i, k) + dfs(k+1, j) + maxarray[i][k] * maxarray[k+1][j])
            dp[i][j] = tmp
            return tmp
                
        return dfs(0, len(arr) - 1)