// https://leetcode.com/problems/stone-game-v

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + stoneValue[i])
        def dfs(i, j):
            if i == j:
                return 0
            if dp[i][j]:
                return dp[i][j]
            tmp = float("-inf")
            for k in range(i, j):
                sum1 = prefix[k+1] - prefix[i]
                sum2 = prefix[j+1] - prefix[k+1]
                if sum1 < sum2:
                    tmp = max(tmp, dfs(i, k) + sum1)
                elif sum1 > sum2:
                    tmp = max(tmp, dfs(k+1, j) + sum2)
                else:
                    tmp = max(tmp, dfs(i, k) + sum1, dfs(k+1, j) + sum2)
            dp[i][j] = tmp
            return tmp
        
        ans = dfs(0, n-1)
        return ans