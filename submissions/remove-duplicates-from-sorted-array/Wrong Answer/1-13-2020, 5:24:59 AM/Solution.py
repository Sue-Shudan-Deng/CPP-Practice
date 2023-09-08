// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        快慢指针
        """
        lo = 0
        for hi in range(len(nums)):
            if nums[lo] == nums[hi]:
                hi += 1
            else:
                nums[lo] = nums[hi]
                lo += 1
        return lo + 1