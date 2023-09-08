// https://leetcode.com/problems/permutations

class Solution {
    
private:
    vector<vector<int>> ans;
    void backtrack(vector<int>& nums, set<int>& visited, vector<int> cur) {
        if (cur.size() == nums.size()) {
            ans.push_back(cur);
            return;
        }
        for (auto n : nums) {
            if (!visited.count(n)) {
                visited.insert(n);
                cur.push_back(n);
                backtrack(nums, visited, cur);
                visited.erase(n);
                cur.pop_back();
            }
        }
    }
    
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> cur;
        set<int> visited;
        backtrack(nums, visited, cur); 
        return ans;
    }
};