// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
#         """
#         method 1: naive DFS
#         """
#         def isPalindrome(s: str, l: int, r: int) -> bool:
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True
                
#         ans, n = [], len(s)
#         def dfs(cur: List[str], start: int, ans: List[List[str]]):
#             if start == n:
#                 ans.append(cur[:])
#             for end in range(start, n):
#                 if isPalindrome(s, start, end):
#                     # set
#                     cur.append(s[start:end + 1])
#                     dfs(cur, end + 1, ans)
#                     # clear
#                     cur.pop()
#         dfs([], 0, ans)
#         return ans
    
        """
        method 2: DFS + memorization
        """
        ans, n = [], len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        def dfs(cur: List[str], start: int, ans: List[List[str]]):
            if start == n:
                ans.append(cur[:])
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start+1][end-1]):
                    # set
                    dp[start][end] = True
                    cur.append(s[start:end + 1])
                    dfs(cur, end + 1, ans)
                    # clear
                    cur.pop()
        dfs([], 0, ans)
        return ans