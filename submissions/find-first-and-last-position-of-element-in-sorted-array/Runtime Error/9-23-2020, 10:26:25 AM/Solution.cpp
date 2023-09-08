// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
    
private:
    int search(vector<int>& nums, int target, bool left) {
        int l = 0, r = nums.size() - 1, m = 0;
        while (l < r) {
            m = l + (r - l) / 2;
            if (left) {
                if (nums[m] >= target) {
                    r = m;
                } else {
                    l = m + 1;
                }
            } else{
                if (nums[m] > target) {
                    r = m;
                } else{
                    l = m + 1;
                }
            }
        }
        if (left) {
            return nums[l] == target ? l : -1;
        } else {
            return nums[l-1] == target ? l-1 : -1;
        }
    }
    
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = search(nums, target, true);
        int r = search(nums, target, false);
        
        return vector<int>{l ,r};
    }
};