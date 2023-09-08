// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        
        if (len1 > len2) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int l = 0, r = len1, m1 = 0, m2 = 0;
        while (l <= r) {
            m1 = l + (r - l) / 2;
            m2 = (len1 + len2 + 1) / 2 - m1;
            auto num1_1 = m1 > 0 ? nums1[m1 - 1] : INT_MIN;
            auto num1_2 = m1 < len1 ? nums1[m1] : INT_MAX;
            auto num2_1 = m2 > 0 ? nums2[m2 - 1] : INT_MIN;
            auto num2_2 = m2 < len2 ? nums2[m2] : INT_MAX;
            
            if (num1_1 > num2_2) {
                r = m1 - 1;
            } else if (num1_2 < num2_1) {
                l = m1 + 1;
            } else {
                // 那么则表示所有应该满足的条件都满足了
                if ((len1 + len2) % 2 == 0) {
                    return static_cast<double>(max(num1_1, num2_1) + min(num1_2, num2_2)) / 2.0;
                } else {
                    return static_cast<double>(max(num1_1, num2_1));
                }
            }
        }
        return 0.0;
    }
};