// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        XOR是关键
        """
        x, y = int(a, 2), int(b, 2) # 换成二进制int表示
        while y:
            answer = x ^ y # 做XOR运算本质上是没有carry的加法，再做一次XOR即可加上carry
            carry = (x & y) << 1 # 求carry bit的方法
            x, y = answer, carry
        return bin(x)[2:]  # 换成二进制str表示并去掉0b