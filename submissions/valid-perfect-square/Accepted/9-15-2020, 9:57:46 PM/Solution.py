// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            m = l + (r - l) // 2
            if m ** 2 == num:
                return m
            elif m ** 2 > num:
                r = m - 1
            else:
                l = m + 1