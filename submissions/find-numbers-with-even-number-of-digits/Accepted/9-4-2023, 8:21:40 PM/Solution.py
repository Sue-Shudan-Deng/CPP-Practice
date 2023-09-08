// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        num = 0
        
        for integer in nums:
            digits = 1
            while integer/10 >= 1:
                digits += 1
                integer = integer/10
        
            if digits%2 == 0:
                num += 1
        
        return num
    
