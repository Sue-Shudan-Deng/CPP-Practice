// https://leetcode.com/problems/toss-strange-coins

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        Target sum
        """
        n = len(prob)
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0] = [1 for _ in range(target + 1)]
        for i in range(1, n + 1):
            if target == 0:
                # 只可能反面
                dp[i][0] += dp[i-1][0] * (1 - prob[i-1])
            else:
                for j in range(target):
                    # 正面
                    dp[i][j+1] += dp[i-1][j] * prob[i-1]
                    # 反面
                    dp[i][j] += dp[i-1][j] * (1 - prob[i-1])
        return dp[n][target]