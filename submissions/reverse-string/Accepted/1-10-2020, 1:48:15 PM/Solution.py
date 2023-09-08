// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        用两根指针来做: 首尾swap之后分别前进一格
        """
        def helper(l, r):
            if not l >= r:
                s[l], s[r] = s[r], s[l]
                helper(l+1, r-1)
        helper(0, len(s)-1)