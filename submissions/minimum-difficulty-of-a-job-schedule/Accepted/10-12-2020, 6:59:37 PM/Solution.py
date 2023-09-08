// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], D: int) -> int:
        n = len(jobDifficulty)
        if D > n:
            return -1
        dp = [[float("inf") for _ in range(n)] for _ in range(D + 1)]
        dp[1] = [max(jobDifficulty[0:i+1]) for i in range(n)]
        for k in range(2, D + 1):
            for i in range(1, n):
                for j in range(i):
                    dp[k][i] = min(dp[k][i], dp[k-1][j] + max(jobDifficulty[j+1:i+1]))
        return dp[D][-1]