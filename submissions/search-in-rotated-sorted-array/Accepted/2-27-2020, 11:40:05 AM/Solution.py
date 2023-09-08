// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        https://www.youtube.com/watch?v=7XOQIMZVIjA
        """
        left = 0
        right = len(nums)  - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] >= nums[0] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] >= nums[0] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1