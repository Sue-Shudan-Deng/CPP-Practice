// https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        难点主要在编程上
        all的用法
        """
        for n in nums:
            if all(n >= 2 * x for x in nums if x != n):
                return nums.index(n)
            
        return -1