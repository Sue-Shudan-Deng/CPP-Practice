// https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        P = [[False] * len(s)] * len(s)
        length = 0
        ans = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
            	if j - i < 2:
            		P[i][j] = (s[i] == s[j])
            	else:
            		P[i][j] = self.longestPalindrome(s[i+1:j]) and (s[i] == s[j])
            	if P[i][j] and j - i > length:
            		length = j - i
            		ans = s[i:j+1] 
        return ans        