// https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        res = int(re.sub(r'[^0-9\-]', ' ', s).split()[0])
        if res > (pow(2,31) - 1):
            return sys.maxsize
        elif res < -pow(2,31):
            return -sys.maxsize - 1
        else:
            return res