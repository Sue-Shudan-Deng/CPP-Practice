// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        XOR是关键
        """
        x, y = int(a, 2), int(b, 2) # 换成二进制int表示
        return bin(x + y)[2:]  # 换成二进制str表示并去掉0b