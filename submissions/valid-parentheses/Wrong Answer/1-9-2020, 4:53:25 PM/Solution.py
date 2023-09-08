// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in mapping:
                top = stack.pop() if stack else "#"
                if not top == mapping[i]:
                    return False
            else:
                stack.append(i)
        return True