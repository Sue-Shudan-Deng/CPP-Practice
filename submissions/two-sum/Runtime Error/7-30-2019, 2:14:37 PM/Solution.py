// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a, i in enumerate(nums):
            if target - i in nums and not (target - i == i):
                b = nums.index(target - i)
                break
        return [a, b]
        