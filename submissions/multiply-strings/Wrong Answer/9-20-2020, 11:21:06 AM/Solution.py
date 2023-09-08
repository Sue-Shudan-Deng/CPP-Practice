// https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = collections.defaultdict(int)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                res[i+j] += (mul % 10)
                res[i+j+1] += (mul // 10)
        s = ""
        for k in res:
            if res[k]:
                s += str(res[k])
        return s