// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp_pal = [[False for _ in range(n)] for _ in range(n)]
        dp_mem = [float("inf") for _ in range(n + 1)]
        def dfs(start: int):
            if start == n:
                return
            cnt = 0
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp_pal[start+1][end -1]):
                    dp_pal[start][end] = True
                    cnt += 1
                    if dp_mem[end] == float("inf"):
                        dfs(end+1)
            dp_mem[start] = cnt
        
        dfs(0)
        ans = 0
        for i in range(n):
            ans += dp_mem[i]
        return ans