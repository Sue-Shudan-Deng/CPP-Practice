// https://leetcode.com/problems/missing-ranges

class Solution {
    
private:
    string generate_range(int lower, int upper) {
        if (lower == upper) {
            return to_string(lower);
        } else {
            return to_string(lower) + "->" + to_string(upper);
        }
    }
    
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string> res;
        int n = nums.size();
        if (n == 0) {
            res.push_back(generate_range(lower, upper));
            return res;
        }
        char cur;
        if (lower < nums[0]) {
            res.push_back(generate_range(lower, nums[0]-1));
        }
        for (int i = 1; i < n; ++i) {
            if (nums[i] > lower && nums[i] > nums[i-1]+1) {
                res.push_back(generate_range(nums[i-1]+1, nums[i]-1));
            }
        }
        if (upper > nums.back()) {
            res.push_back(generate_range(nums.back()+1, upper));
        }
        return res;
    }
};