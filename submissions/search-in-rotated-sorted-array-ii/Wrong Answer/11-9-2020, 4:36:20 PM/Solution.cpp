// https://leetcode.com/problems/search-in-rotated-sorted-array-ii

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        // Step 1: search the smallest element 
        int l = 0, r = nums.size() - 1; 
        int m = 0;
        while (l < r) {
            m = l + (r - l) / 2;
            if (nums[m] < nums[r]) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        
        cout << l;
        
        // Step 2 : search target with shortened range
        int smallest_idx = l;
        l = 0, r = nums.size() - 1;
        if (target < nums[r]) {
            l = smallest_idx;
        } else if (target > nums[r]) {
            r = smallest_idx - 1;
        } else {
            return r;
        }
        
        while (l < r) {
            m = l + (r - l) / 2;
            if (nums[m] >= target) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return nums[l] == target ? l : -1;
    }
};