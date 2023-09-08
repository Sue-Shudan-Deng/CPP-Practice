// https://leetcode.com/problems/powx-n

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def fastpow(x, n):
            if n == 0:
                return 1 
            half = fastpow(x, n // 2)
            if n % 2:
                return half * half * x
            else:
                return half * half
        if n < 0:
            x, n = 1 / x, -n
        return fastpow(x, n)