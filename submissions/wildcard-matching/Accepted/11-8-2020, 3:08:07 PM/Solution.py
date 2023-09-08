// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        dp = [[False for _ in range(np + 1)] for _ in range(ns + 1)]
        dp[0][0] = True
        if ns == 0 and np == 0:
            return True
        if np == 0:
            return False
        for j in range(1, np + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                # if match
                if p[j-1] == "?" or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # if not match
                if p[j-1] == "*":
                    # case 1: empty sequence
                    dp[i][j] = dp[i][j-1]
                    # case 2: length >= 1
                    dp[i][j] |= dp[i-1][j]
        return dp[-1][-1]