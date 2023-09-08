// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2
            if left:
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1
        return r

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        right_idx = self.extreme_insertion_index(nums, target, False) - 1
        return [left_idx, right_idx]