// https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        # make sure abs(a) >= abs(b)
        sign = 1 if a > 0 else 0
        if a * b > 0:
            while y:
                ans = x ^ y
                carry = (x & y) << 1
                x, y = ans, carry
        else:
            while y:
                ans = x ^ y
                carry = ((~x) & y) << 1
                x, y = ans, carry
        return ans * sign
            