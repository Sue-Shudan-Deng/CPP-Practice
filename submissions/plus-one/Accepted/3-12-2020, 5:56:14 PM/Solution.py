// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums, cnt = copy.deepcopy(digits), 0
        while nums and nums.pop() == 9:
            cnt += 1
        if cnt == 0:
            return digits[:-1] + [digits[-1] + 1]
        elif cnt != len(digits):
            idx = len(digits) - cnt - 1
            return digits[:idx] + [digits[idx] + 1] + [0] * cnt
        else:
            return [1] + [0] * len(digits)