// https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def P(self, s):
        if len(s) <=2:
            return s[0] == s[-1]
        else:
            return self.P(s[1:-1]) and s[0] == s[-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        P = [[False] * len(s)] * len(s)
        length = 0
        if s == "":
            return s
        ans = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                P[i][j] = self.P(s[i:j+1])
                if P[i][j] and j - i > length:
                    length = j - i
                    ans = s[i:j+1] 
        return ans