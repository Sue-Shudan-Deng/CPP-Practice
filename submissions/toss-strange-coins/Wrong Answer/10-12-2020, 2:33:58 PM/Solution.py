// https://leetcode.com/problems/toss-strange-coins

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        0 / 1 bounded knapsack, weight is prob
        """
        n = len(prob)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(n):
            for j in range(target, 0, -1):
                dp[j] += dp[j - 1] * prob[i]
        return dp[target]