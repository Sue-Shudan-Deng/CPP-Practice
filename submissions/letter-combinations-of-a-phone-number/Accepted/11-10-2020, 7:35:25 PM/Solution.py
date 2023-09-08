// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
        
        ans = []
        def backtrace(start, cur):
            if start == len(digits):
                ans.append(cur[:])
                return

            for ch in phone[digits[start]]:
                backtrace(start + 1, cur + ch)
                
        backtrace(0, "")
        return ans if digits != "" else []