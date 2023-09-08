// https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        largest = 0
        second_largest = 0
        for k, n in enumerate(nums[1:]):
            if n > nums[largest]:
                second_largest = largest
                largest = k + 1
                
        return largest if nums[largest] >= 2 * nums[second_largest] else -1   