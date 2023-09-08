// https://leetcode.com/problems/search-in-rotated-sorted-array-ii

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        
        // https://www.youtube.com/watch?v=e-UALGfQpOk
        // 解决方法居然是删除掉后面的元素即可
        
        if (nums.size() == 0) {
            return false;
        }
        
        int j = nums.size() - 1;
        while (j > 0 && nums[j] == nums[0]) {
            --j;
        }
        
        // Step 1: search the smallest element 
        int l = 0, r = j; 
        int m = 0;
        while (l < r) {
            m = l + (r - l) / 2;
            if (nums[m] <= nums[r]) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        
        // Step 2 : search target with shortened range
        int smallest_idx = l;
        l = 0, r = j;
        if (target < nums[r]) {
            l = smallest_idx;
        } else if (target > nums[r]) {
            r = smallest_idx - 1;
        } else {
            return true;
        }
        
        while (l < r) {
            m = l + (r - l) / 2;
            if (nums[m] >= target) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return nums[l] == target ? true : false;
    }
};