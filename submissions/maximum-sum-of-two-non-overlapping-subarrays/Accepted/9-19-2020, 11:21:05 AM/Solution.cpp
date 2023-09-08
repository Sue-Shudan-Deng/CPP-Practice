// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays

class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& A, int L, int M) {
        if (A.size() < L + M) {
            return 0;
        }
        int cnt = 0;
        int n = A.size();
        vector<int> prefix(n+1, 0);
        for (int i = 0; i < n; ++i) {
            cnt += A[i];
            prefix[i+1] = cnt;
        }
        vector<vector<int>> dp(n+1, vector<int>(2, 0));
        // 这里有两种方案
        // 第一种是我使用当前位置的后L个作为L数组，然后反复迭代确定前i-L中最大的M数组
        // 第一种是我使用当前位置的后M个作为M数组，然后反复迭代确定前i-M中最大的L数组
        int Lmax = prefix[L];
        int Mmax = prefix[M];
        int res = 0;
        for (int i = L+M; i <= n; ++i) {
            Lmax = max(Lmax, prefix[i-M] - prefix[i-M-L]);
            Mmax = max(Mmax, prefix[i-L] - prefix[i-M-L]);
            res = max(res, max(Lmax + prefix[i] - prefix[i-M], 
                               Mmax + prefix[i] - prefix[i-L]));
        }
        return res;
    }
};