// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

class Solution(object):
    def isconsect(self, nums):
        x = sorted(nums)
        return len(x) == len(set(x)) and x[-1] - x[0] == len(x) - 1

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
            y = list(sorted(set(nums)))
            x = y
            if len(x) < k:
                return False
            else:
                while (len(x) >= k):
                    for v in x[:k]:
                        del nums[nums.index(v)]
                    x = list(sorted(set(nums)))
                return self.isconsect(y[:k]) and self.isPossibleDivide(nums, k)