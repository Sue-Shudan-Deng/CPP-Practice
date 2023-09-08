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
    
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         """
#         分治法，iteration版本
#         """
#         def fastPow(x: float, n: int):
#             if n == 0:
#                 return 1
#             ans = 1
#             curr = x
#             powrange = []
#             while n:
#                 powrange.append(n)
#                 n //= 2
            
#             # 这里面的运算比较巧妙
#             for i in powrange:
#                 if i % 2:
#                     ans *= curr
#                 curr = curr * curr
#             return ans
                
#         if n < 0:
#             x, n = 1 / x, -n
#         return fastPow(x, n)