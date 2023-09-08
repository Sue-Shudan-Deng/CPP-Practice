// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        recursion
        这里python没办法像c++那样直接用n//2，因为-1//2 = -1
        """
        def fastPow(x: float, n: int):
            if n == 0:
                return 1
            half = fastPow(x, n//2)
            if n % 2:
                return half * half * x
            else:
                return half * half
    
        if n < 0:
            x, n = 1 / x, -n
        return fastPow(x, n)