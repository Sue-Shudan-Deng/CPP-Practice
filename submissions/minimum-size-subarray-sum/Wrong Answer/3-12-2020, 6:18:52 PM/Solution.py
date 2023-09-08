// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        summ, i, ans = 0, 0, float("inf")
        for j, n in enumerate(nums):
            summ += n
            while summ >= s:
                ans = min(ans, j - i + 1)
                summ -= nums[i]
                i += 1
        return ans if nums else 0