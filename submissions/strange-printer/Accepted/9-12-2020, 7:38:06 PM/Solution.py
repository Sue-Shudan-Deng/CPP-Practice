// https://leetcode.com/problems/strange-printer

class Solution:
    def strangePrinter(self, s: str) -> int:
        if s == "":
            return 0
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i < n - 1:
                dp[i][i+1] = 1 if s[i] == s[i+1] else 2
                
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                dp[left][right] = right-left+1  # maximum possible number
                for k in range(left, right):
                    tmp = dp[left][k] + dp[k+1][right]
                    if s[k] == s[right]:
                        tmp -= 1
                    dp[left][right] = min(dp[left][right], tmp)
        return dp[0][-1]