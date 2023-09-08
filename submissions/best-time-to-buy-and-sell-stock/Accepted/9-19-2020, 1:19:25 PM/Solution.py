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
    
    # """
    # method 2: DP. 参考https://www.youtube.com/watch?v=8pVhUpF1INw method2
    # """
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     minprice = float("inf")
    #     dp = [0 for _ in range(n + 1)]
    #     for i in range(1, n + 1):
    #         minprice = min(minprice, prices[i-1])
    #         dp[i] = max(dp[i-1], prices[i-1] - minprice)
    #     return dp[-1]
    
#     """
#     method 3: DP. 参考https://www.youtube.com/watch?v=8pVhUpF1INw method3
#     """
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         n = len(prices)
#         gain = [0] + [prices[i] - prices[i-1] for i in range(1, n)]
#         dp = [0 for _ in range(n+1)]
#         for i in range(1, n+1):
#             dp[i] = max(dp[i-1] + gain[i-1], gain[i-1])
#         return max(dp[1:])
    
    
    """
    method 4. DP. 本人认为最直接的DP，但需要依赖一点数学
    """
    def maxProfit(self, prices: List[int]) -> int:
        # dp表示截止到i为止，最大的profit是多少，那么就可以包含num[i]或者不包含num[i]
        # dp[i] = max(dp[i-1], max(prices[i] - prices[j]) for j in range(i-1))
        #       = max(dp[i-1], prices[i] + max(-prices[j]))
        # 由于i > j，那么可以用一个变量tmp来专门迭代max(-prices[j])
        n = len(prices)
        dp = [0 for _ in range(n+1)]
        tmp = float("-inf")
        for i in range(1, n+1):
            dp[i] = max(dp[i-1], prices[i-1] + tmp)
            tmp = max(tmp, -prices[i-1])
        return dp[-1]