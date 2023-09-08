// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        思路参见buy-and-sell-stock-i and dicussion
        """
        # K-dim DP
        # dp[k][i] = max(dp[k][i-1], max(dp[k-1][j]+prices[i]-prices[j] for j in range(i-1)))
        #          = max(dp[k][i-1], prices[i] + max(dp[k-1][j]-prices[j]))
        n, K = len(prices), 2
        dp = [[0 for _ in range(n+1)] for _ in range(K+1)]
        for k in range(1, K+1):
            tmp = float("-inf")
            for i in range(1, n+1):
                dp[k][i] = max(dp[k][i-1], prices[i-1] + tmp)
                tmp = max(tmp, dp[k-1][i] - prices[i-1])
        return dp[K][-1]