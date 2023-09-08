// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        """
        lo = 0
        for hi in range(1, len(nums)):
            if nums[hi] != nums[lo]:
                lo += 1
                nums[lo] = nums[hi]
        return lo + 1