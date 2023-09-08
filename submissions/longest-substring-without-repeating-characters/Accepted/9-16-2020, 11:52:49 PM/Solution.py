// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        ans, i = 0, 0
        for j in range(len(s)):
            if s[j] in m:
                i = max(i, m.get(s[j]))
            m[s[j]] = j + 1
            ans = max(ans, j-i+1)
        return ans