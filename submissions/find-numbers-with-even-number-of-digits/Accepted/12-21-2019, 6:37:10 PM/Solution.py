// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = list(map(lambda x: len(str(x)), nums))
        return len(list(filter(lambda x: x % 2 == 0, digits)))