// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        这类题可归类为子部分顺序翻转
        做法是全局reverse + 部分reverse
        方法1: build-in
        """
        return "".join(reversed(s.split()))
    

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        这类题可归类为子部分顺序翻转
        做法是全局reverse + 部分reverse
        方法1: build-in
        """
        return " ".join(reversed(s.split()))
    
    
        