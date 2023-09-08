// https://leetcode.com/problems/decode-string

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num, curr, stack = 0, "", []
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char == "[":
                stack.append(curr)
                stack.append(str(num))
                curr, num = "", 0 # unset
            elif char == "]":
                cnt = stack.pop()
                pre_str = stack.pop()
                curr = pre_str + cnt * curr
            else:
                curr += char
        return curr