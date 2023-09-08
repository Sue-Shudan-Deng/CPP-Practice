// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = []
        res = 0
        ans = 0
        for i in s:
            if not i in num:
                num.append(i)
                res += 1
                ans = max(ans, res)
            else:
                idx = num.index(i)
                res -= idx
                num = num[idx+1:]
                num.append(i)
        return ans