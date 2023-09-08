// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                nums[k] = nums[i]
                k += 1
                
        return k            