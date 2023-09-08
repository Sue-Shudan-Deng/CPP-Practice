// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(map(lambda x: "".join(reversed(list(x))), s.split())))