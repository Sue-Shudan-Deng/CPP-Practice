// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        这里的DP变成了记录当前break point下所有可能的组合
        """
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if len(dp[j]) > 0 and s[j:i] in wordDict:
                    for p in dp[j]:
                        dp[i].append(p + ("" if p == "" else " ") + s[j:i])
        return dp[len(s)]