// https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def bs(l: int, r: int) -> int:
            m = (l + r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                return bs(m+1, r)
            else:
                return bs(l, m-1)
        return bs(1, n)