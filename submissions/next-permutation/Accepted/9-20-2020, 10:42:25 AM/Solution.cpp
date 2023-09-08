// https://leetcode.com/problems/next-permutation

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        bool val = std::next_permutation(nums.begin(), nums.end()); 
        if (val == false) {
            std::sort(nums.begin(), nums.end());
        }
    }
};