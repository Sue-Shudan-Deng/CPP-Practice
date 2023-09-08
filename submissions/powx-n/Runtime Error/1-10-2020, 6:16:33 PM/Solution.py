// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        return x * self.myPow(x, n-1)