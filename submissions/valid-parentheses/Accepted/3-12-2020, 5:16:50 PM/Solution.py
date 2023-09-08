// https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in mapping and stack:
                j = stack.pop()
                if j != mapping[i]:
                    return False
            else:
                stack.append(i)
        return stack == []
            
        