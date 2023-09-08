// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        ans, i = 0, 0
        for j in range(len(s)):
            if s[j] in m:
                i = max(i+1, m.get(s[j])+1)
            m[s[j]] = j
            ans = max(ans, j-i+1)
        return ans