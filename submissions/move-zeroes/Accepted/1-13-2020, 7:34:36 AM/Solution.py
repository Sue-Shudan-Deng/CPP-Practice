// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for n in nums:
            if n == 0:
                cnt += 1
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                
        for c in range(1, cnt + 1):
            nums[-c] = 0