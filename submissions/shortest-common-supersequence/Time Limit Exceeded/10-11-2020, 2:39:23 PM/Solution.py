// https://leetcode.com/problems/shortest-common-supersequence

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        dp = [["" for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = ""
        for i in range(1, n1 + 1):
            dp[i][0] = str1[:i]
        for j in range(1, n2 + 1):
            dp[0][j] = str2[:j]
        
        # dp[i][j], the shortest string str1[:i] and str2[:j] can form
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j], key = len) + str1[i-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + str1[i-1] + str2[j-1], dp[i][j-1] + str2[j-1], dp[i-1][j] + str1[i-1], key=len)
        return dp[-1][-1]