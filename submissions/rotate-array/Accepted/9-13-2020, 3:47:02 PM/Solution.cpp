// https://leetcode.com/problems/rotate-array

class Solution {
    
private:
    void reverse(vector<int>& nums, int left, int right) {
        while (left < right) {
            swap(nums[left++], nums[right--]);
        }
    }
    
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        reverse(nums, 0, nums.size()-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, nums.size()-1);
    }
};