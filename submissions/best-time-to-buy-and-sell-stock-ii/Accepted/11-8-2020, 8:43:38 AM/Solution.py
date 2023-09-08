// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        method 1
        """
        # minprice = float("inf")
        # cnt = 0
        # for price in prices:
        #     if price < minprice:
        #         minprice = price
        #     else:
        #         cnt += price - minprice
        #         minprice = price
        # return cnt
    
        """
        method 2: use gain array
        """
        n = len(prices)
        gain = [prices[i] - prices[i-1] for i in range(1, n)]
        return sum([i for i in gain if i > 0])