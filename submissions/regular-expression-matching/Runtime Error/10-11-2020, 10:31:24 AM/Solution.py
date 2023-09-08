// https://leetcode.com/problems/regular-expression-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        dp = [[False for _ in range(np + 1)] for _ in range(ns + 1)]
        dp[0][0] = True
        if p[0] == "*":
            return False
        
        for j in range(1, np + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j] or dp[0][j-1] or dp[0][j-2]
        
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == "*" and p[j-2] != "*":
                    # case 0: zero or one of preceding element
                    dp[i][j] = dp[i][j-1] or dp[i][j-2]
                    # case 1: multiple of preceding element
                    if s[i-1] == s[i-2] and (p[j-2] == "." or s[i-2] == p[j-2]):
                        dp[i][j] = dp[i][j] or dp[i-1][j-1] or dp[i-1][j]
                    else:
                        if p[j-2] == ".":
                            dp[i][j] = dp[i][j] or dp[i-1][j-1]
        return dp[-1][-1]