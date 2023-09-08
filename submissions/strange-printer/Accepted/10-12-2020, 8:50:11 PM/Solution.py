// https://leetcode.com/problems/strange-printer

class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        https://leetcode.com/problems/strange-printer/discuss/106810/Java-O(n3)-DP-Solution-with-Explanation-and-Simple-Optimization
        """
        if s == "":
            return 0
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i < n - 1:
                dp[i][i+1] = 1 if s[i] == s[i+1] else 2
                
        for l in range(n-2, -1, -1):
            for r in range(l+2, n):
                dp[l][r] = r - l + 1  # maximum possible number
                for k in range(l, r):
                    if s[k] == s[r]:
                        tmp = dp[l][k] + dp[k+1][r-1]  # dp[r][r-1] = 0
                    else:
                        tmp = dp[l][k] + dp[k+1][r]
                    # 这里的意思是，如果s[k] == s[r]，那么k和right可以在同一次操作中被                         打印出, 因为dp[r][r] = 1
                    dp[l][r] = min(dp[l][r], tmp)
        return dp[0][-1]