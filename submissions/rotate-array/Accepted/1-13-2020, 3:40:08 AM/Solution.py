// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        最优解法这里用了reverse的办法，正常情况下不太可能想得到
        """
        def reverse(nums: List[int]):
            lo = 0
            hi = len(nums) - 1
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo, hi = lo + 1, hi - 1
            return nums
            
        k = k % len(nums)
        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])