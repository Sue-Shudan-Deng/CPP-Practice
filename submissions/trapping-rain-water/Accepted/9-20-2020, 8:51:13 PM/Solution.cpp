// https://leetcode.com/problems/trapping-rain-water

class Solution {
public:
    int trap(vector<int>& height) {
        int l_max = 0, r_max = 0;
        int n = height.size();
        int l = 0, r = n - 1;
        int ans = 0;
        while (l < r) {             
            if (height[l] > l_max) {
                l_max = height[l];
            }
            if (height[r] > r_max) {
                r_max = height[r];
            }
            if (l_max < r_max) {
                // 放心计算左边
                ans += max(0, l_max - height[l]);
                ++l;
            } else {
                // 放心计算右边
                ans += max(0, r_max - height[r]);
                --r;                
            }
        }
        return ans;
    }
};