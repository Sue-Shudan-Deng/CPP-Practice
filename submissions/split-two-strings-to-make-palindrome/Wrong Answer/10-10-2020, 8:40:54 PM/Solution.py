// https://leetcode.com/problems/split-two-strings-to-make-palindrome

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if b == b[::-1] or (a + b[len(a):]) == (a + b[len(a):])[::-1]:
            return True
        n, flagA, flagB, testA, testB = len(a), True, True, True, True
        for i in range(n):
            if testA and i <= n-i and a[i] != b[n-i-1]:
                flagA = b[i:n-i] == b[i:n-i][::-1]
                testA = False
            if testB and i <= n-i and b[i] != a[n-i-1]:
                flagB = a[i:n-i] == a[i:n-i][::-1]
                testB = False
        return flagA or flagB