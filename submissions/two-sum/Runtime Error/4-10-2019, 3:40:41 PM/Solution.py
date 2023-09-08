// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        half = int(target/2)
        if nums.count(half) == 2:
            return list(filter(lambda x: x==half, nums))
        elif nums.count(half) == 1:
            ele = list(filter(lambda x: target-x in nums and x!=half, nums))
            return [nums.index(ele[0]), nums.index(ele[1])]
        else:
            ele = list(filter(lambda x: target-x in nums, nums))
            return [nums.index(ele[0]), nums.index(ele[1])]
        