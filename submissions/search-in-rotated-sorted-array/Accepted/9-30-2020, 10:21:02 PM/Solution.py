// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        https://www.youtube.com/watch?v=QdVrY3stDD4&t=1s
        """
        # step1: search through the smallest element
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
                
        smallest_idx = l
        l, r = 0, len(nums) - 1
        # step2: bianry search on target
        if target <= nums[r]:
            l = smallest_idx
        else:
            r = smallest_idx - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l if nums[l] == target else -1