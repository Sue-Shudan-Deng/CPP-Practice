// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1;
        ret = 1
        if n % 2:
            ret = x if n > 0 else 1/x
        half = self.myPow(x, n//2)
        ret *= half * half
        return ret
    
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