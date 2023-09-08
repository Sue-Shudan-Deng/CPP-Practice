// https://leetcode.com/problems/burst-balloons

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int left = n - 3; left >= 0; --left) {
            for (int right = left + 2; right < n; ++right) {
                for (int mid = left + 1; mid < right; ++mid) {
                    dp[left][right] = max(dp[left][right], dp[left][mid] + nums[left] * nums[mid] * nums[right] + dp[mid][right]);
                }
            }
        }
        return dp[0][n-1];
    }
};