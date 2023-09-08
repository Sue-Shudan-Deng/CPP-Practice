// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        chardict = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        charlist = list(chardict.keys())
        
        length = len(s)
        i = 0
        res = 0
        while(i < length):
            if i < length - 1 and s[i] + s[i + 1] in charlist:
                res += chardict[s[i] + s[i+1]]
                i += 2
            else:
                res += chardict[s[i]]
                i += 1
            
        return res