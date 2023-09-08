// https://leetcode.com/problems/palindrome-partitioning-ii

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp_pal = [[0 for _ in range(n)] for _ in range(n)]
        dp_cut = [float("inf") for _ in range(n + 1)]
        dp_cut[n] = -1
        def dfs(start: int, ans: int) -> int:
            if start == n:
                return dp_cut[n]
            tmp = float("inf")
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp_pal[start+1][end-1]):
                    dp_pal[start][end] = True
                    if dp_cut[end + 1] == float("inf"):
                        tmp = min(tmp, dfs(end + 1, ans + 1) + 1)
                    else:
                        tmp = min(tmp, dp_cut[end + 1] + 1)
            dp_cut[start] = tmp
            return tmp
                        
        return dfs(0, 0)    