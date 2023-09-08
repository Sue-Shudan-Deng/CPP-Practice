// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str, l: int, r: int):
            return all(s[l+k] == s[r-k] for k in range((r-l) // 2))
        
        n = len(s)
        for i in range(n // 2):
            j = n - 1 - i
            if i < j and s[i] != s[j]:
                return isPalindrome(s, i + 1, j) or isPalindrome(s, i, j - 1)
        return True