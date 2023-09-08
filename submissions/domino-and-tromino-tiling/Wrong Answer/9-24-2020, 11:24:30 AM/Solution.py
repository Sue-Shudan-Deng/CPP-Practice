// https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
    def numTilings(self, N: int) -> int:
        # https://www.youtube.com/watch?v=__yxFFRQAl8&t=817s
        if N == 0:
            return 0
        if N == 1:
            return 1
        dp = [[0 for _ in range(3)] for _ in range(N)]
        dp[0][0], dp[1][0] = 1, 2
        for i in range(2, N):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]
            dp[i][1] = dp[i-2][0] + dp[i-1][2]
            dp[i][2] = dp[i-2][0] + dp[i-1][1]
            
        return sum(dp[-1])
        