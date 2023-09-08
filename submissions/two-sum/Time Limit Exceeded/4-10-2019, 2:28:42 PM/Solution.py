// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_nums = [i for i, s in enumerate(nums)]
        return list(filter(lambda x: list(filter(lambda y: y!= x and nums[x] + nums[y] == target, index_nums)), index_nums))
        