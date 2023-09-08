// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        def dfs(start: int):
            if start == n:
                return
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start+1][end -1]):
                    dp[start][end] = True
                    dfs(end+1)
        
        dfs(0)
        ans = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    ans += 1
        return ans