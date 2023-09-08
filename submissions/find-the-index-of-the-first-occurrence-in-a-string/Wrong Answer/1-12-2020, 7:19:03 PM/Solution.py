// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        L = len(needle)
        if n == 0:
            return 0
        
        for start in range(n-L):
            if haystack[start:start+L] == needle:
                return start
        return -1