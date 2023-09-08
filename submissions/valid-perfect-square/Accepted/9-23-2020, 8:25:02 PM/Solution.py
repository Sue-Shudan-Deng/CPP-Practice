// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l < r:
            m = l + (r - l) // 2
            if m ** 2 >= num:
                r = m
            else:
                l = m + 1
        
        return True if l ** 2 == num else False