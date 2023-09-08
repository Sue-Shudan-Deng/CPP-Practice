// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_nums = [i for i, s in enumerate(nums)]
        half = list(filter(lambda x: nums[x] + nums[x] == target, index_nums))
        if len(half) == 2:
            return half
        elif len(half) == 1:
            return list(filter(lambda x: target-nums[x] in nums and 2*nums[x]!=target, index_nums))
        else:
            return list(filter(lambda x: target - nums[x] in nums, index_nums))
        