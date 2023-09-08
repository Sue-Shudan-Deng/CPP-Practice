// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
#         """
#         method 1: naive backtrack
#         """
#         def isPalindrome(s: str, l: int, r: int) -> bool:
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True
                
#         ans, n = [], len(s)
#         def backtrack(cur: List[str], start: int, ans: List[List[str]]):
#             if start == n:
#                 ans.append(cur[:])
#             for end in range(start, n):
#                 if isPalindrome(s, start, end):
#                     # set
#                     cur.append(s[start:end + 1])
#                     backtrack(cur, end + 1, ans)
#                     # clear
#                     cur.pop()
#         backtrack([], 0, ans)
#         return ans
    
        """
        method 2: backtrack + memorization
        可以按照combination类型的思路来答题, 即，使用start
        """
        ans, n = [], len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        def backtrack(cur: List[str], start: int, ans: List[List[str]]):
            if start == n:
                ans.append(cur[:])
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    backtrack(cur + [s[start:end + 1]], end + 1, ans)
        backtrack([], 0, ans)
        return ans