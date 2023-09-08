// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        cnt = 0
        for price in prices:
            if price < minprice:
                minprice = price
            else:
                cnt += price - minprice
                minprice = price
        return cnt