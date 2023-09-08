// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing

class Solution {
    
// private:
//     int ans;
//     void dfs(vector<int>& A, vector<int>& B, int i, int c) {
//         if (c >= ans) {
//             // no need to continue
//             return;
//         }
//         if (i == A.size()) {
//             ans = min(ans, c);
//             return;
//         } 
        
//         if ((i == 0) || (A[i] > A[i-1] && B[i] > B[i-1])) {
//             dfs(A, B, i + 1, c); // no need ti switch
//         }
        
//         if ((i == 0) || (B[i] > A[i-1] && A[i] > B[i-1])) {
//             swap(A[i], B[i]);
//             dfs(A, B, i + 1, c+1);
//             swap(A[i], B[i]);
//         }
//     }
    
// public:
//     int minSwap(vector<int>& A, vector<int>& B) {
//         ans = INT_MAX;
//         dfs(A, B, 0, 0);
//         return ans;
//     }
    
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        vector<vector<int>> dp(A.size(), vector<int>(2, INT_MAX));
        // DP[i][0]: keep   DP[i][1]: swap
        dp[0][0] = 0;
        dp[0][1] = 1;
        for (int i = 1; i < A.size(); ++i) {
            if (A[i] > A[i-1] && B[i] > B[i-1]) {
                dp[i][0] = min(dp[i-1][0], dp[i][0]);
                dp[i][1] = min(dp[i-1][1] + 1, dp[i][1]); 
            }
            
            if (B[i] > A[i-1] && A[i] > B[i-1]) {
                dp[i][0] = min(dp[i-1][1], dp[i][0]);   // 由于上一行已经初始化了所以这里用min
                dp[i][1] = min(dp[i-1][0] + 1, dp[i][1]);
            }
        }
        return min(dp.back()[0], dp.back()[1]);
    }
};