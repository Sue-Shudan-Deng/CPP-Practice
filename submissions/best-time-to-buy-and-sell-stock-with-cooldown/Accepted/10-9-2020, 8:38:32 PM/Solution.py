// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=oL6mRyTn56M&t=6s
        """
        n = len(prices)
        hold = [0 for _ in range(n + 1)]
        sell = [0 for _ in range(n + 1)]
        rest = [0 for _ in range(n + 1)]
        hold[0] = float("-inf") # -inf 仅表示这个状态不合法
        
        for i in range(1, n + 1):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i-1])
            sell[i] = hold[i-1] + prices[i-1]
            rest[i] = max(rest[i-1], sell[i-1])
            
        return max(sell[-1], rest[-1])