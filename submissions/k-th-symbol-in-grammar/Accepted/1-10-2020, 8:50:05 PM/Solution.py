// https://leetcode.com/problems/k-th-symbol-in-grammar

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 and K == 1:
            return 0
        if K > 2**(N-2):
            prev_K = K - 2**(N-2)
            return 1 - self.kthGrammar(N-1, prev_K)
        else:
            prev_K = K
            return self.kthGrammar(N-1, prev_K) 