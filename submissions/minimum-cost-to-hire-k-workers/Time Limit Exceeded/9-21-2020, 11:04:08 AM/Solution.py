// https://leetcode.com/problems/minimum-cost-to-hire-k-workers

class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        ans = float('inf')

        N = len(quality)
        for captain in range(N):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = Fraction(wage[captain], quality[captain])
            prices = []
            for worker in range(N):
                price = factor * quality[worker]
                if price < wage[worker]: continue
                prices.append(price)

            if len(prices) < K: continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))

        return float(ans)
        