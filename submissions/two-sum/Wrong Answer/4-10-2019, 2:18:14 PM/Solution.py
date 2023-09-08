// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ele = list(filter(lambda x: list(filter(lambda y: y!= x and x + y == target, nums)), nums))
        return [i for i, s in enumerate(nums) if s in ele]
        