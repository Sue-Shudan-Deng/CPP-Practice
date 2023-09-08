// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        ans, i = 0, 0
        # "abba"
        for j in range(len(s)):
            if s[j] in m:
                # 确保i至少是j的下一个元素，太巧妙
                i = max(i, m.get(s[j])+1)
            m[s[j]] = j
            ans = max(ans, j-i+1)
        return ans