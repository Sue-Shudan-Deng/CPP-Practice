// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def valid(s: str):
            return 1 <= int(s) and int(s) <= 26
        
        n = len(s)
        if n == 1:
            return valid(s)
        if n == 2:
            return (valid(s[0]) and valid(s[1])) + valid(s)
        
        dp = [0 for _ in range(n)]
        dp[0] = valid(s[0])
        dp[1] = (valid(s[0]) and valid(s[1])) + valid(s[-2:])
        for i in range(2, n):
            if valid(s[i]):
                dp[i] += dp[i-1]
            if valid(s[-2:]):
                dp[i] += dp[i-2]
        print(dp)
        return dp[-1]