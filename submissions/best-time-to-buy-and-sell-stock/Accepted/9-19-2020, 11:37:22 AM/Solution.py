// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0
        for price in prices:
            if price <= minprice:
                minprice = price
                continue
            if price - minprice >= maxprofit:
                maxprofit = price - minprice
        return maxprofit