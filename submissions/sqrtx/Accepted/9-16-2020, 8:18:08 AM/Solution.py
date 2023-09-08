// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 1, x
        while l <= r:
            m = l + (r - l) // 2
            # 收敛条件
            if m**2 == x or (m**2 < x and (m+1)**2 > x):
                return m
            # 左移条件
            elif m**2 > x:
                r = m-1
            # 右移条件
            else:
                l = m+1