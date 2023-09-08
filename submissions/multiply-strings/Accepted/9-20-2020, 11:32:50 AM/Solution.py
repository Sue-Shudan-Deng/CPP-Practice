// https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = collections.defaultdict(int)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                res[i+j] += (mul // 10)
                res[i+j+1] += (mul % 10)
        s, carry = "", 0
        for i in range(m+n-1, -1, -1):
            s += str((res[i] + carry) % 10)
            carry = (res[i] + carry) // 10
        return str(int(s[::-1])) # just to remove leading zeros, can be improved when interviewed