// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def P(self, s: str) -> str:
        if self.P_store.get(s) == None:
            if len(s) <= 2:
                self.P_store[s] = s[0] == s[-1]
            else:
                self.P_store[s] = self.P(s[1:-1]) and s[0] == s[-1]
        return self.P_store[s]

    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s
        self.P_store = dict()
        length = 0
        ans = s[0]
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                s_bar = s[i:j+1]
                if self.P(s_bar) and j - i > length:
                    length = j - i
                    ans = s_bar
        return ans
        