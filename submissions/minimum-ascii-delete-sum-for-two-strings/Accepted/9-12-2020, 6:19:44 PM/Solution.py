// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for k, i in enumerate(s1):
            dp[k+1][0] = dp[k][0] + ord(i);
        for k, j in enumerate(s2):
            dp[0][k+1] = dp[0][k] + ord(j)
            
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), 
                                   dp[i][j-1] + ord(s2[j-1]), \
                                   dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), \
                                   dp[i][j-1] + ord(s2[j-1]), \
                                   dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1]))
        return dp[-1][-1]