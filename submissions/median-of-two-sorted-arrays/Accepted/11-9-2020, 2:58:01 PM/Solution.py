// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        https://www.youtube.com/watch?v=ScCg9v921ns
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            # always search in the smaller size array
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, len1
        
        """
        这道题的难点在于 r = len1 - 1 而不是 r = len1，如果写成后者是错的
        原因是，这道分界线其实可以划在最后一个元素的后面和最前面一个元素的前面，
        跟最常规的不能数组越界是不一样的
        """
        
        while l <= r:
            m1 = l + (r - l) // 2            # 该nums1分界线左边的元素有多少个
            m2 = (len1 + len2 + 1) // 2 - m1 # 该nums2分界线左边的元素有多少个
            nums1_1 = nums1[m1-1] if m1 > 0 else float("-inf")
            nums1_2 = nums1[m1] if m1 < len1 else float("inf")
            nums2_1 = nums2[m2-1] if m2 > 0 else float("-inf")
            nums2_2 = nums2[m2] if m2 < len2 else float("inf")
            if nums1_1 > nums2_2:
                r = m1 - 1
            elif nums2_1 > nums1_2:
                l = m1 + 1
            else:
                if (len1 + len2) % 2 == 0:
                    return (max(nums1_1, nums2_1) + min(nums1_2, nums2_2)) / 2
                else:
                    return max(nums1_1, nums2_1)