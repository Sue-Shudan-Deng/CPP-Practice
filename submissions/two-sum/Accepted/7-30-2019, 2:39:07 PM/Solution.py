// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a, i in enumerate(nums):
            x = nums[:(nums.index(i))] + nums[(nums.index(i))+1:]
            if target - i in x:
                b = x.index(target - i) + 1
                break
        return [a, b]
        