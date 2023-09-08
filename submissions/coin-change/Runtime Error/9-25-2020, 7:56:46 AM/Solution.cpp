// https://leetcode.com/problems/coin-change

class Solution {
    
private:
    int n;
    vector<int> dp;
    
public:
    int coinChange(vector<int>& coins, int amount) {
        n = coins.size();
        dp = vector<int>(amount + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = coins[i]; j <= amount; ++j) {
                dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }
        
        return dp.back();
    }
};