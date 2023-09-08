// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

class Solution:
    def maxProfit(self, K: int, prices: List[int]) -> int:
        n = len(prices)
        # solve special cases
        if not prices or K == 0:
            return 0
        if 2*K > n:
            """
            退化到 best time to bell and sell stock II
            """
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res
        
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