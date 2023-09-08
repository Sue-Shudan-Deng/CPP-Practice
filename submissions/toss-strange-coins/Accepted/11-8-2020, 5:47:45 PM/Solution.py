// https://leetcode.com/problems/toss-strange-coins

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        0 / 1 bounded knapsack，灵活
        """
        n = len(prob)
        dp = [0 for _ in range(target + 1)]
        # dp[k] = dp[k - 1] * p + dp[k] * (1 - p)
        dp[0] = 1
        for p in prob:
            for k in range(target, -1, -1):
                # k == 0: 只可能是反面
                dp[k] = (dp[k-1] * p if k > 0 else 0) + dp[k] * (1 - p)
        return dp[target]