// https://leetcode.com/problems/distinct-subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        dp = [[0 for _ in range(nt + 1)] for _ in range(ns + 1)]
        """
        1. S = "rabbbit", T = "", ans = 1, https://www.youtube.com/watch?v=mPqqXh8XvWY
        2. 不管s当前的元素是啥，我们总可以skip掉它，因为题目仅仅要求一个subsequence
        """
        for i in range(ns + 1):
            dp[i][0] = 1
        for i in range(1, ns + 1):
            for j in range(1, nt + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]