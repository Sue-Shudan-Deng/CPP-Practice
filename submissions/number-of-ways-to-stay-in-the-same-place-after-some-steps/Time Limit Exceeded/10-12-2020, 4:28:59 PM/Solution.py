// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [[0 for _ in range(arrLen)] for _ in range(steps + 1)]
        dp[0][0], mod = 1, 10**9 + 7
        dirs = [-1, 0, 1]
        for s in range(1, steps + 1):
            for i in range(arrLen):
                for d in dirs:
                    new_i = i + d
                    if 0 <= new_i < arrLen:
                        dp[s][new_i] = (dp[s][new_i] + dp[s-1][i]) % mod
        return dp[s][0]