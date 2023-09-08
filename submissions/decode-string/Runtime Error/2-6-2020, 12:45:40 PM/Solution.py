// https://leetcode.com/problems/decode-string

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr = ""
        num = 0
        stack = []
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append(curr)
                stack.append(str(num))
                print stack
                curr = ""
                num = 0
            elif char == ']':
                cnt = int(stack.pop())
                pre = stack.pop()
                curr = pre + cnt * curr
                stack.append(curr)
            else:
                curr += char
        return curr