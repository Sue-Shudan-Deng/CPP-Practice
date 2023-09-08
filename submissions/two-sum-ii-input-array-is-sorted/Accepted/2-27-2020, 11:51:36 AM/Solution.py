// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            summ = numbers[lo] + numbers[hi]
            if summ < target:
                lo += 1
            elif summ > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]  
        return []