// https://leetcode.com/problems/split-two-strings-to-make-palindrome

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a) > len(b):
            return self.checkPalindromeFormation(b, a)
        
        if b == b[::-1] or (a + b[len(a):]) == (a + b[len(a):])[::-1]:
            return True
        na, nb, flagA, flagB = len(a), len(b), True, True
        for i in range(na):
            if i <= nb-i and a[i] != b[nb-i-1]:
                flagA = b[i:nb-i] == b[i:nb-i][::-1]
            if i <= na-i and b[i] != a[na-i-1]:
                flagB = a[i:na-i] == a[i:na-i][::-1]
        return flagA or flagB