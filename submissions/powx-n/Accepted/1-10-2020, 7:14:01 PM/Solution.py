// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        分治法，recursion版本
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
    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        分治法，iteration版本，这算法老奸巨猾
        """
        def fastPow(x: float, n: int):
            if n == 0:
                return 1
            ans = 1
            curr = x
            # 因为python特性的原因，没有自定义的for循环参数，
            # 故提前声明一个range
            powrange = []
            while n:
                powrange.append(n)
                n //= 2
            print(powrange)
            for i in powrange:
                if i % 2:
                    ans *= curr
                curr = curr * curr
            return ans
                
        if n < 0:
            x, n = 1 / x, -n
        return fastPow(x, n)