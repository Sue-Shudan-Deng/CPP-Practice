// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p =  bisect.bisect_right(nums, target)
        return p if nums[p] != target else p - 1