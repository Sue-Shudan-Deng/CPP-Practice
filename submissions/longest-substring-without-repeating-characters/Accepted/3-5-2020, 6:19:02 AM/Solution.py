// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        summ = 0
        ans = 0
        nums = []
        for char in s:
            if not char in nums:
                nums.append(char)
                summ += 1
                ans = max(ans, summ)
            else:
                idx = nums.index(char)
                summ -= idx
                nums = nums[idx + 1:]
                nums.append(char)
        return ans