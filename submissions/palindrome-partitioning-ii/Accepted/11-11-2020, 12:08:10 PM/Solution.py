// https://leetcode.com/problems/palindrome-partitioning-ii

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp_pal = [[0 for _ in range(n)] for _ in range(n)]
        dp_cut = [-1 for _ in range(n + 1)]
        def dfs(start: int, ans: int) -> int:
            if start == n:
                return -1
            tmp = float("inf")
            for idx in range(start, n):
                if s[start]==s[idx] and (idx-start<=2 or dp_pal[start+1][idx-1]):
                    dp_pal[start][idx] = True
                    if dp_cut[idx + 1] == -1:
                        tmp = min(tmp, dfs(idx + 1, ans + 1) + 1)
                    else:
                        tmp = min(tmp, dp_cut[idx + 1] + 1)
            dp_cut[start] = tmp
            return dp_cut[start]
                        
        dfs(0, 0)
        return dp_cut[0]