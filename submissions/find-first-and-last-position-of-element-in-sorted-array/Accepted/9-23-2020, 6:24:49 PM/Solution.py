// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        l, r = 0, len(nums) 
        """
        这里因为后面r要减1，所以r的初始值取len(nums)也是很重要的，否则一定取不到nums[-1]
        """
        while l < r:
            m = l + (r - l) // 2
            # 其实无非就是相等的时候左移还是右移
            if left:
                if nums[m] >= target:  # lower bound
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] > target:   # upper bound
                    r = m
                else:
                    l = m + 1
        return l
    
    """
    本质：https://www.youtube.com/watch?v=v57lNF2mb_s&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=15
    lower bound 和 upper bound
    """

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        """
        这里的edge case的判断非常巧妙
        """
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        right_idx = self.extreme_insertion_index(nums, target, False) - 1
        return [left_idx, right_idx]