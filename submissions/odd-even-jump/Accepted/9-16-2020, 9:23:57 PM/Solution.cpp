// https://leetcode.com/problems/odd-even-jump

class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        int n = A.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[n-1][0] = 1;
        dp[n-1][1] = 1;
        map<int, int> m;
        m[A[n-1]] = n-1;
        int ans = 1;
        
        for (int i = n-2; i >= 0; --i) {
            auto up_jump = m.lower_bound(A[i]);
            if (up_jump != m.end()) {
                dp[i][0] = dp[up_jump->second][1];
                // 我去，iterator作为指针还可以这么用，牛逼
            }
            
            auto down_jump = m.upper_bound(A[i]);
            if (down_jump != m.begin()) {
                dp[i][1] = dp[prev(down_jump)->second][0];
            }
            
            if (dp[i][0] == 1) {
                ++ans;
            }
            m[A[i]] = i;
        }
        return ans;
    }
};