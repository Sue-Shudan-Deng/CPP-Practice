// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i = 1
        nums = []
        while i**2 <= x:
            nums.append(i)
            i += 1
        l, r = 1, x
        while l <= r:
            m = (l + r) // 2
            if m**2 <= x and (m+1)**2 > x:
                return m
            elif x <= (m+1)**2:
                r = m-1
            else:
                l = m+1