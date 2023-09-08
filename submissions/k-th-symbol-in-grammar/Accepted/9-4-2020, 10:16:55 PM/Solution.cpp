// https://leetcode.com/problems/k-th-symbol-in-grammar

// recursion

// kthGrammar(N, K) = kthGrammar(N-1, K-2^N-1) or kthGrammar(N-1, K)    

class Solution {
public:
    int kthGrammar(int N, int K) {
        if (N == 1) return 0;
        if (K > pow(2, N-2)) {
            return 1 - kthGrammar(N, K-pow(2, N-2));
        } else {
            return kthGrammar(N-1, K);
        }
    }
};