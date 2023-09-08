// https://leetcode.com/problems/stone-game-iv

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False]*(n+1)
        for i in range(n+1):
            if dp[i]:
                continue
            for k in range(1, int(n**0.5)+1):
                if i+k*k <= n:
                    dp[i+k*k] = True
                else:
                    break
        return dp[n]