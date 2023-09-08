// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        https://www.youtube.com/watch?v=7XOQIMZVIjA
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if target >= nums[0]:
                if nums[m] >= nums[0] and target > nums[m]:
                    # nums[0] <= nums[m] < target， 正常顺序
                    l = m+1
                else:
                    # nums[0] <= target
                    r = m-1
            else:
                if nums[m] >= nums[0] or target > nums[m]:
                    # nums[0] > target > nums[m], 4,5,6,0,1,2,3, target=3
                    # nums[m] > nums[0] > target, 4,5,6,7,1,2,3, target=3
                    l = m+1
                else:
                    r = m-1
        return -1