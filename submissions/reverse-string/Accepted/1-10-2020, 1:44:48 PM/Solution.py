// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        用两根指针来做: 首尾swap之后分别前进一格
        """
        left = 0
        right = len(s) - 1
        while not left == right and not left == right + 1 :
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1 