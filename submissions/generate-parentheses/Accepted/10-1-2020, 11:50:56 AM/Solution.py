// https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = set()
        def backtrack(S = "", left = 0, right = 0):
            if left == n and right == n:
                ans.add(S)
            if left < n:
                backtrack(S + "(", left + 1, right)
            if right < left:
                backtrack(S + ")", left, right + 1)
        backtrack()
        return list(ans)