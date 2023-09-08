// https://leetcode.com/problems/palindrome-partitioning-iii

class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        """
        https://www.youtube.com/watch?v=kD6ShM6jr3g
        其实感觉和 Best time to buy and sell stock 类似 
        """
        def minChange(i, j):
            c = 0
            while i < j:
                if s[i] != s[j]:
                    c += 1
                i += 1
                j -= 1
            return c
        
        if K >= len(s):
            return 0
        
        n = len(s)
        dp = [[float("inf") for _ in range(n)] for _ in range(K + 1)]
        dp[1] = [minChange(0, i) for i in range(n)]
        for k in range(2, K + 1):
            for i in range(1, n):
                for j in range(i):
                    dp[k][i] = min(dp[k][i], dp[k-1][j] + minChange(j+1, i))
        return dp[K][-1]