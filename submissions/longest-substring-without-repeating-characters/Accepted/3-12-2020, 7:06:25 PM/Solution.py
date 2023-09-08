// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, num, res = float("-inf"), [], 0
        for char in s:
            if not char in num:
                num.append(char)
                res += 1
                ans = max(ans, res)
            else:
                idx = num.index(char)
                num = num[idx + 1:]
                num.append(char)
                res -= idx
        return ans if s else 0