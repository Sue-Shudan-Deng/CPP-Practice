// https://leetcode.com/problems/trapping-rain-water

class Solution {
public:
    int trap(vector<int>& height) {
        int l_max = 0, r_max = 0;
        int n = height.size();
        int l = 0, r = n - 1;
        int ans = 0;
        while (l < r) { 
            while (l < r && height[l] < l_max) {
                ans += (l_max - height[l]);
                ++l;
            }
            while (l < r && height[r] < r_max) {
                ans += (r_max - height[r]);
                --r;
            }
            
            if (height[l] > l_max) {
                l_max = height[l];
            }
            
            if (height[r] > r_max) {
                r_max = height[r];
            }
            ++l;
            --r;
        }
        return ans;
    }
};