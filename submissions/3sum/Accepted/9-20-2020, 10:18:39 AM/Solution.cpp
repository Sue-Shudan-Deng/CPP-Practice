// https://leetcode.com/problems/3sum

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        if (n <= 2) {
            return res;
        }
        for (int i = 0; i < n-2; ++i) {
            int l = i+1, r = n-1;
            if (nums[i] + nums[i+1] + nums[i+2] > 0) {
                break;
            }
            if (nums[i] + nums[n-2] + nums[n-1] < 0 || (i > 0 && nums[i] == nums[i-1])) {
                continue;
            }
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] == 0) {
                    res.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    while (l+1 < r && nums[l] == nums[l+1]) {
                        ++l;
                    }
                    while (r-1 > r && nums[r] == nums[r-1]) {
                        --r;
                    }
                    ++l;
                    --r;
                } else if (nums[i] + nums[l] + nums[r] < 0) {
                    ++l;
                } else {
                    --r;
                }
            }
        }
        return res;
    }
};