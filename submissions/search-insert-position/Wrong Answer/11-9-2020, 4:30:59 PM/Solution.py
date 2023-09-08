// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - 1