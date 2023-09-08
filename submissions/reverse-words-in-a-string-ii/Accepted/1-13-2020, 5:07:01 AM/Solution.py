// https://leetcode.com/problems/reverse-words-in-a-string-ii

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Step1: reverse function 
        def reverse(l: list, left: int, right: int):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left + 1, right - 1
                
        # Step2: reverse each word
        def reverse_each_word(l: list) -> None:
            """
            双指针
            """
            lo, hi = 0, 0
            n = len(l)
            
            while lo < n:
                while hi < n and l[hi] != ' ':
                    hi += 1
                reverse(l, lo, hi - 1)
                lo = hi + 1  # 需要+1是因为有个空格
                hi += 1
                
        reverse(s, 0, len(s) - 1)
        reverse_each_word(s)