// https://leetcode.com/problems/toss-strange-coins

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        Target sum
        """
        n, offset = len(prob), 1
        dp = [[0 for _ in range(target + 1 + offset)] for _ in range(n + 1)]
        dp[0] = [1 for _ in range(target + 1 + offset)]
        for i in range(1, n + 1):
            for j in range(target + 1 + offset - 1):
                # 正面
                dp[i][j+1] += dp[i-1][j] * prob[i-1]
                # 反面
                dp[i][j] += dp[i-1][j] * (1 - prob[i-1])
        return dp[n][target]