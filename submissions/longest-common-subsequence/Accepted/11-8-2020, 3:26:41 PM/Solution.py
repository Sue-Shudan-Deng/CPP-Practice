// https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1, set2 = set(text1), set(text2)
        if not set1.intersection(set2):
            return 0
        
        n1, n2 = len(text1), len(text2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max([dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1])
                else:
                    dp[i][j] = max([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]])
                
        return dp[-1][-1]