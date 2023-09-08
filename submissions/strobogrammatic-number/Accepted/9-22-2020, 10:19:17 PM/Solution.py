// https://leetcode.com/problems/strobogrammatic-number

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"6":"9", "9":"6", "1":"1", "8":"8", "0":"0"}
        return "".join(num[::-1]) == "".join([mapping.get(n, "") for n in num])