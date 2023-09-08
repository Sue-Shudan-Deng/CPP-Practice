// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice, maxprofit = float("inf"), 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice >= maxprofit:
                maxprofit = price - minprice
        return maxprofit