// https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = set()
        def bt(curr = [], left = 0, right = 0):
            if left > n or right > n:
                return
            if left == n and right == n:
                res.add(curr[:])
            if left < n:
                bt(curr + '[', left + 1, right)
            if right < left:
                bt(curr + ']', left, right + 1)
        bt()
        return res