// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

class Solution:
    def maxProfit(self, K: int, prices: List[int]) -> int:
        n = len(prices)
        if K - n > 0:
            K = K - n
        dp = [[0 for _ in range(n + 1)] for _ in range(K + 1)]
        """
        dp[k][i] = max(dp[k][i-1], max(dp[k-1][j] + prices[i] - prices[j] for j in range(0, i-1))
        """
        for k in range(1, K+1):
            tmp = float("-inf")
            for i in range(1, n+1):
                dp[k][i] = max(dp[k][i-1], prices[i-1] + tmp)
                tmp = max(tmp, dp[k-1][i] - prices[i-1])
        return dp[-1][-1]