// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        """
        lo = 1
        for hi in range(1, len(nums)):
            print(lo, hi)
            print(nums[lo], nums[hi])
            if nums[hi] != nums[lo]:
                nums[lo] = nums[hi]
                lo += 1

        return lo