// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                # 非常非常巧妙
                # 保证了每次搜索范围总是缩小的
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1
        return nums[l]