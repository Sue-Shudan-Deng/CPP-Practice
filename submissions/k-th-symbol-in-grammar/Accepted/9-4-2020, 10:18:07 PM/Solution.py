// https://leetcode.com/problems/k-th-symbol-in-grammar

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if K > 2**(N-2):
            return 1 - self.kthGrammar(N-1, K-2**(N-2))
        else:
            return self.kthGrammar(N-1, K)