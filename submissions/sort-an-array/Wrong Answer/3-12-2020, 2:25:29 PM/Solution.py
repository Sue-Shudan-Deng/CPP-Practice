// https://leetcode.com/problems/sort-an-array

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        方法一：bottom-up merge sort 
        """
        def merge(nums1, nums2):
            res = []
            l, r = 0, 0
            while l < len(nums1) and r < len(nums2):
                if nums1[l] < nums2[r]:
                    res.append(nums1[l])
                    l += 1
                else:
                    res.append(nums2[r])
                    r += 1
            res.extend(nums1[l:])
            res.extend(nums2[r:])
            return res
        
        size = 1
        while size < len(nums):
            size *= 2
            for pos in range(0, len(nums), size):
                start = pos 
                mid = pos + size // 2
                end = pos + size
                nums[start:end] = merge(nums[start:mid], nums[mid:end])
        return nums
    
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        方法二：quick sort 
        """
        return self.qsort(nums, 0, len(nums) - 1)
    
    def qsort(self, nums, lo, hi):
        if lo < hi:
            q = self.partition(nums, lo, hi)
            self.qsort(nums, lo, q)
            self.qsort(nums, q + 1, hi)
            
    def partition(self, nums, lo, hi):
        pivot = lo
        lo += 1
        while True:
            while lo <= hi and nums[lo] <= nums[pivot]:
                lo += 1
            while lo <= hi and nums[hi] >= nums[pivot]:
                hi -= 1
            if lo <= hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
            else:
                break
        # 返回high点
        nums[hi], nums[pivot] = nums[pivot], nums[hi]
        return hi