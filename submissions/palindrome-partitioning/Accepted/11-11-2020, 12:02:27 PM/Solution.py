// https://leetcode.com/problems/palindrome-partitioning

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = []
        def dfs(start, cur):
            if start == n:
                ans.append(cur[:])
                return
            for idx in range(start, n):
                if s[start] == s[idx] and (idx-start <= 2 or dp[start+1][idx-1]):
                    dp[start][idx] = True
                    dfs(idx + 1, cur + [s[start:idx+1]])
                    
        dfs(0, [])
        return ans