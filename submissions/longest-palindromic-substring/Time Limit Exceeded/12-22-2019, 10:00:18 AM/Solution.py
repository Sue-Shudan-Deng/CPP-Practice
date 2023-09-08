// https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def P(self, s):
        if self.P_store.get(s) != None:
            return self.P_store[s]
        else:
            if len(s) <= 2:
                self.P_store[s] = s[0] == s[-1]
                return self.P_store[s]
            else:
                self.P_store[s] = self.P(s[1:-1]) and s[0] == s[-1]
                return self.P_store[s]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        P = [[False] * len(s)] * len(s)
        self.P_store = dict()
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