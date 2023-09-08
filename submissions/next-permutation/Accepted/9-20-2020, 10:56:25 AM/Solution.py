// https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = n-2, n-1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1;
        if i >= 0:
            while j > i and nums[j] <= nums[i]:
                j -= 1
            if j > i:
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])
        return nums