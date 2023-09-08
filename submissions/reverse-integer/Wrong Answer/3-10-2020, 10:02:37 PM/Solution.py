// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
            return - int((str(x)[1:])[::-1]) if x < 0 else int(str(x)[::-1])