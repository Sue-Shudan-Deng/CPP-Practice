// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict()
        for k, v in enumerate(nums):
            mapping[v] = k
        for k, n in enumerate(nums):
            if mapping.get(target - n) and mapping.get(target - n) != k:
                return k, mapping.get(target - n)