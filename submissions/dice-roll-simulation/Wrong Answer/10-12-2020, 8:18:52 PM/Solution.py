// https://leetcode.com/problems/dice-roll-simulation

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        method 1: https://www.youtube.com/watch?v=3JOZcD-BRLE
        """
        mod = 10 ** 9 + 7
        dp = [[[0 for _ in range(15)] for _ in range(6)] for _ in range(n + 1)]
        # dp[i][j][k]: length i, k's consecutive j at the end
        for j in range(6):
            dp[1][j][1] = 1
            
        for i in range(2, n + 1):
            for j in range(6):
                for p in range(6): 
                    for k in range(1, rollMax[p] + 1):
                        if p != j:
                            dp[i][j][1] = dp[i][j][1] + dp[i-1][p][k]
                        else:
                            if k < rollMax[p]:
                                dp[i][j][k+1] += dp[i-1][j][k]
        return sum([sum(i) for i in dp[n]])