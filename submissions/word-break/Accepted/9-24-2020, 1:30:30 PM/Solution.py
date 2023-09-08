// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, wordDict_ = len(s), set(wordDict)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict_:
                k = len(w)
                if i >= k and w == s[i-k:i]:
                    dp[i] = dp[i] or dp[i-k]
        return dp[-1]