// https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            # 退出条件：l = r
            m = l + (r - l) // 2
            if nums[m] > nums[m+1]:
                # stand here or move left
                r = m
            else:
                # move right
                l = m + 1
        return l