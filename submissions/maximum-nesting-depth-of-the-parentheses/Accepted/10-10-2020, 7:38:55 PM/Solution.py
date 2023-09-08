// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxdepth = 0
        for i in s:
            if i == "(":
                depth += 1
                maxdepth = max(maxdepth, depth)
            elif i == ")":
                depth -= 1
        return maxdepth