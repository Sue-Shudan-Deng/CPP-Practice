// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
                
        ans, n = [], len(s)
        def dfs(cur: List[str], start: int, ans: List[List[str]]):
            if start == n:
                ans.append(cur[:])
            for end in range(start, n):
                if isPalindrome(s, start, end):
                    # set
                    cur.append(s[start:end + 1])
                    dfs(cur, end + 1, ans)
                    # clear
                    cur.pop()
        dfs([], 0, ans)
        return ans