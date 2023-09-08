// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

import copy
class Solution(object):
    def isconsect(self, nums):
        x = sorted(nums)
        return x == sorted(list(set(x))) and x[-1] - x[0] == len(x) - 1

    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == []:
            return True
        new_nums = copy.deepcopy(nums)
        if len(nums) % k != 0:
            return False
        else:
            x = list(set(sorted(new_nums)))
            if len(x) < k:
                return False
            else:
                for v in x[:k]:
                    del new_nums[new_nums.index(v)]
                return self.isconsect(x[:k]) and self.isPossibleDivide(new_nums, k)        