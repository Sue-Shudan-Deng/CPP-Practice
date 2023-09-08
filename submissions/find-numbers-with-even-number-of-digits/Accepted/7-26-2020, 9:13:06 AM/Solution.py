// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([i for i in nums if len(str(i)) % 2 == 0])