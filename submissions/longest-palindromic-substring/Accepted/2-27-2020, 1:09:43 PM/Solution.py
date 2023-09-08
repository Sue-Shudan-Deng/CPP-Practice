// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        expand from center
        """
        def getlen(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l + 1, l + 1, r - 1 
        
        start, end, oldmax = 0, 0, 0
        for i in range(len(s)):
            len1, l1, r1 = getlen(i, i)
            len2, l2, r2 = getlen(i, i + 1)
            newmax = max(len1, len2)
            if newmax > oldmax:
                if len1 > len2:
                    start, end = l1, r1
                else:
                    start, end = l2, r2
                oldmax = newmax
        return s[start: end + 1]