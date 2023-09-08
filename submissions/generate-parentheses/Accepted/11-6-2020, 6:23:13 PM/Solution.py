// https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = set()
        def bt(left = 0, right = 0, S = ""):
            if left == n and right == n:
                ans.add(S)
            if left < n:
                bt(left + 1, right, S + "(")
            if right < left:
                bt(left, right + 1, S + ")")
        bt()
        return list(ans)