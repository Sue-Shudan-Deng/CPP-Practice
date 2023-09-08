// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        for _ in range(n):
            ans *= x
        return ans