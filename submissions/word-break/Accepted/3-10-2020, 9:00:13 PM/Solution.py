// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        自底向上的DP
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]