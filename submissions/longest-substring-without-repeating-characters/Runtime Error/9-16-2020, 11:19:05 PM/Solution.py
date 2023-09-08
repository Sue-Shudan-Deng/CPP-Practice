// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = []
        tmp = 0
        ans = 0
        for i in s:
            if not i in num:
                num.append(i)
                tmp += 1
                ans = max(ans, res)
            else:
                idx = num.index(i)
                tmp -= idx
                num = num[idx+1:]
                num.append(i)
        return ans