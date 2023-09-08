// https://leetcode.com/problems/target-sum

class Solution {
    
private:
    vector<vector<int>> dp;
    
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int summ = accumulate(nums.begin(), nums.end(), 0);
        int target = S + summ;
        if ((S > 0 && S > summ) || (S < 0 && S < -summ) || (target % 2 == 1)) {
            return 0;
        }
        target /= 2;
        dp = vector<vector<int>>(nums.size()+1, vector<int>(target+1, 0));
        
        for (int i = 0; i <= nums.size(); ++i) {
            dp[i][0] = 1;
        }
        for (int i = 1; i <= nums.size(); ++i) {
            copy(dp[i-1].begin(), dp[i-1].end(), dp[i].begin());
            for (int j = nums[i-1]; j <= target; ++j) {
                dp[i][j] += dp[i-1][j-nums[i-1]];
            }
        }
        int maxnum = 0;
        for (int i = 0; i <= nums.size(); ++i) {
            maxnum = max(maxnum, dp[i][target]);
        }
        return maxnum; 
    }
};