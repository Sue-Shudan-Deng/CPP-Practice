// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(n):
            if '0' not in f'{a}{n-a}':
                # f'{a}{n-a}'的意思是，'21'
                # https://realpython.com/python-string-formatting/
                return [a, n-a]