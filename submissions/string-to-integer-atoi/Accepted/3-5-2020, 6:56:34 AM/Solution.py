// https://leetcode.com/problems/string-to-integer-atoi

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        length = len(s)
        res = ""
        i = 0
        # 以字母开头是不合法的，以'+', '-'和数字开头是合法的
        while length > 0:
            if ((i == 0) and (s[i] == '+' or s[i] == '-' or s[i].isdigit())) \
                or (i > 0 and s[i].isdigit()):
                res += s[i]
                i += 1
                length -= 1
            else:
                break
        # 如果一个数字都没找到或者只找到一个'+'或'-'，那么是不合法的
        if len(res) == 0 or (len(res) == 1 and (s[0] == '+' or s[0] == '-')):
            return 0
        else:
             ans = int(res)
        if ans > pow(2,31)-1:
            return pow(2,31)-1
        elif ans < -pow(2,31):
            return -pow(2,31)
        else:
            return ans