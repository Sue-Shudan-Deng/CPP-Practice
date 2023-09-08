// https://leetcode.com/problems/combinations

class Solution {
    
private:
    vector<vector<int>> res;
    void backtrack(vector<int>& cur_comb, int tail, int n, int k) {
        if (cur_comb.size() == k) {
            res.push_back(cur_comb);
            return;
        }
        // set
        for (int right = tail + 1; right <= n; ++right) {
            // set
            cur_comb.push_back(right);
            // backtrack
            backtrack(cur_comb, right, n, k);
            // clear
            cur_comb.pop_back();
        }
    }
    
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> cur_comb;
        backtrack(cur_comb, 0, n, k);
        return res;
    }
};