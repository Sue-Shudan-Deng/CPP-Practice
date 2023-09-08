// https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            # 退出条件：l = r
            m = l + (r - l) // 2
            if nums[m] > nums[m+1]:
                # 一定不能向右了，守住这里
                r = m
            else:
                # 向左没意义，peak一定在右边
                l = m + 1
        return l