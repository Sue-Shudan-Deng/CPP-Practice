// https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        length = len(s)
        res = ""
        ans = 0
        i = 0
        while length > 0:
            if (i == 0 and (s[i] == "-" or s[i] == "+" or s[i].isdigit())) \
               or (i > 0 and s[i].isdigit()):
                res += s[i]
                length -= 1
                i += 1
            else:
                break

        if (len(res) == 1 and (res[0] == "+" or res[0] == "-")) or len(res) == 0:
            return 0
        else:
             ans = int(res)
        if ans > pow(2,31)-1:
            return pow(2,31)-1
        elif ans < -pow(2,31):
            return -pow(2,31)
        else:
            return res