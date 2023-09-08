// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        """
        lo = 1
        print("nums:", nums)
        n = len(nums)
        for hi in range(1, n):
            print("hi:", hi)
            print(lo)
            print("nums:", nums)
            if nums[hi] != nums[lo]:
                nums[lo] = nums[hi]
                lo += 1
            print("nums:", nums)
        return lo