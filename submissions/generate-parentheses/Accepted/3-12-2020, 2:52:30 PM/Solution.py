// https://leetcode.com/problems/generate-parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans  = []
        def helper(curr, left, right):
            if left > n or right > n:
                return
            if left == n and right == n:
                ans.append(curr)
            if left < n:
                helper(curr + "(", left + 1, right)
            if right < left:
                helper(curr + ")", left, right + 1)
        
        helper("", 0, 0)
        return ans