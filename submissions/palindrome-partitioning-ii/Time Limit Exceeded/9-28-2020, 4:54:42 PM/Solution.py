// https://leetcode.com/problems/palindrome-partitioning-ii

class Solution:
    def minCut(self, s: str) -> int:
        n, res = len(s), float("inf")
        dp = [[0 for _ in range(n)] for _ in range(n)]
        def dfs(start: int, ans: int) -> int:
            nonlocal res
            if start == n:
                res = min(res, ans - 1)
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    dfs(end + 1, ans + 1)
        dfs(0, 0)
        return res
                    