// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        The first step here is to check whether s is breakable
        If not, then we should not waste any time doing that
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True      
        if dp[len(s)] == False:
            return []
        """
        这里的dp变成了记录当前break point下所有可能的组合
        """
        dp = [[] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict:
                    if len(dp[j]) == 0:
                        dp[i].append(s[j:i])
                    else:
                        for p in dp[j]:
                            dp[i].append(p + " " + s[j:i])
        return dp[-1]