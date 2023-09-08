// https://leetcode.com/problems/permutations

class Solution {
    
private:
    vector<vector<int>> ret;
    void backtrack(const vector<int>& nums, vector<int>& cur) {
        if (cur.size() == nums.size()) {
            ret.push_back(cur);
            return;
        }
        
        for (auto n : nums) {
            if (find(cur.begin(), cur.end(), n) == cur.end()) {
                // not found
                cur.push_back(n);
                backtrack(nums, cur);
                cur.pop_back();
            }
        }
    }
    
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> cur;
        backtrack(nums, cur);
        return ret;
    }
};