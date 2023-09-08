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
            if char == '[':
                stack.append(curr)
                stack.append(str(num))
                curr = ""
                num = 0
            if char == ']':
                cnt = int(stack.pop())
                pre = stack.pop()
                curr = pre + cnt * curr
                stack.append(curr)
            else:
                curr += char
        return curr