// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0
        for i in prices:
            if prices[i] <= minprice:
                minprice = price[i]
            elif prices[i] - minprice >= maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit