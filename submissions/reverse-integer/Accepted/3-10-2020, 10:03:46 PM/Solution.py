// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        res = - int((str(x)[1:])[::-1]) if x < 0 else int(str(x)[::-1])
        return 0 if (res > pow(2, 31) - 1 or res < - pow(2, 31)) else res