// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        非常经典的一道题
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]