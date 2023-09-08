// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
    
private:
    int search(vector<int>& nums, int target, bool left) {
        int l = 0, r = nums.size(), m = 0;
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
        return l;
    }
    
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return vector<int>{-1, -1};
        }
        
        int l = search(nums, target, true);
        if (l >= 0 and l < nums.size()) {
            l = nums[l] == target ? l : -1;
        }
        int r = search(nums, target, false) - 1;
        if (r >= 0 and r < nums.size()) {
            r = nums[r] == target ? r : -1;
        }
        return vector<int>{l, r};
    }
};