// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        快慢指针
        """
        lo = 0
        for hi in range(len(nums)):
            if nums[lo] != nums[hi]:
                nums[lo] = nums[hi]
                lo += 1
                
        nums = nums[:lo+1]
        print(nums)
        return lo + 1