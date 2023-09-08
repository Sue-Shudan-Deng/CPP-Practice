// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 0, x + 1
        while l < r:
            m = l + (r - l) // 2
            # 左移条件
            if (m + 1) ** 2 > x:
                r = m
            # 右移条件
            else:
                l = m + 1
        return l