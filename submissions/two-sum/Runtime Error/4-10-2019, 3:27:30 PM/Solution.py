// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_nums = [i for i, _ in enumerate(nums)]
        index_nums = [i for i, _ in enumerate(nums)]
        half = int(target/2)
        if (half in nums) and (not nums.remove(half) in half):
            return list(filter(lambda x: target-nums[x] in nums and 2*nums[x]!=target, index_nums))
        else:
            return list(filter(lambda x: target - nums[x] in nums, index_nums))
        