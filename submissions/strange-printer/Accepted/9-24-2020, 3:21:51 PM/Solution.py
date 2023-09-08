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
                
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                dp[left][right] = right-left+1  # maximum possible number
                for k in range(left, right):
                    if s[k] == s[right]:
                        tmp = dp[left][k] + dp[k+1][right-1]
                    else:
                        tmp = dp[left][k] + dp[k+1][right]
                    # 这里的意思是，如果s[k] == s[right]，那么k和right可以在同一次操作中被打印出
                    # 因为dp[right][right] = 1
                    dp[left][right] = min(dp[left][right], tmp)
        return dp[0][-1]