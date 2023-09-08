// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    # """
    # method 1: one pass
    # """
    # def maxProfit(self, prices: List[int]) -> int:
    #     minprice = float("inf")
    #     maxprofit = 0
    #     for price in prices:
    #         if price <= minprice:
    #             minprice = price
    #             continue
    #         if price - minprice >= maxprofit:
    #             maxprofit = price - minprice
    #     return maxprofit
    
    """
    method 2: DP. 参考https://www.youtube.com/watch?v=8pVhUpF1INw method2
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minprice = float("inf")
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            minprice = min(minprice, prices[i-1])
            dp[i] = max(dp[i-1], prices[i-1] - minprice)
        return dp[-1]