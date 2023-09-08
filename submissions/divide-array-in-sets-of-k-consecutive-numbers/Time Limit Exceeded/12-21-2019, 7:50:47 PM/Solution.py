// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

class Solution(object):
    def isconsect(self, nums):
        return len(nums) == len(set(nums)) and max(nums) - min(nums) == len(nums) - 1

    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == []:
            return True
        if len(nums) % k != 0:
            return False
        else:
            x = list(sorted(set(nums)))
            if len(x) < k:
                return False
            else:
                while (len(list(filter(lambda t: t in nums, x[:k]))) == k):
                    for v in x[:k]:
                        del nums[nums.index(v)]
                return self.isconsect(x[:k]) and self.isPossibleDivide(nums, k)