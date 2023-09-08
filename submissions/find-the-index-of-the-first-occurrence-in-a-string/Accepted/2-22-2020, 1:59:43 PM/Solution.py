// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        L = len(needle)
        if L == 0:
            return 0
        for start in range(n-L+1):
            if haystack[start:start+L] == needle:
                return start
        return -1