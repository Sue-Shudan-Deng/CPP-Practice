// https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        numdict = {1: "I", 4: "IV", 5:"V", 9: "IX", 10:"X", 40: "XL", 50:"L", 90: "XC", 100:"C", 400:"CD", 500:"D", 900: "CM", 1000:"M"}
        numlist = list(numdict.keys())
        
        def reduce(num):
            if num in numdict:
                return 0, numdict[num]
            elif num > 1000:
                return num - 1000, numdict[1000] 
            else:
                for i in range(len(numlist) - 1):
                    if numlist[i] < num and num < numlist[i + 1]:
                        return num - numlist[i], numdict[numlist[i]]

        res = ""
        while (num > 0):
            num, s = reduce(num)
            res += s
        return res