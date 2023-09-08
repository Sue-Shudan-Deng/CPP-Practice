// https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Method 1: heap, O(nlogK)
        """
        # return heapq.nlargest(k, nums)[-1]
    
        """
        Method 2: binary search 
        """
        # l, r = -2**31, 2**31-1
        # while l < r:
        #     m, c = l + (r - l) // 2, 0
        #     for num in nums:
        #         if num > m:
        #             c += 1
        #     if c <= k-1:
        #         r = m
        #     else:
        #         l = m + 1
        # return l
        """
        Method 3: quick sort 
        """
        
        """
        Method 4: quick select
        """
        p = self.qselect(nums, 0, len(nums)-1, k) # 一定要注意，python是按引用传递的，不是按值传递，因此nums的值会修改
        return nums[p]

    def qselect(self, nums, lo, hi, k):
        if lo == hi:
            return lo
        if lo < hi:
            p = self.partition(nums, lo, hi)
            if p == len(nums) - k:
                return p
            elif p > len(nums) - k:
                return self.qselect(nums, lo, p - 1, k)
            else:
                return self.qselect(nums, p + 1, hi, k)
    
    def partition(self, lst, lo, hi):
        """
        简单双向版本，pivot取lo
        实践证明面试一定不要尝试三数取中法，edge case太麻烦
        http://www.cs.armstrong.edu/liang/animation/web/QuickSortPartition.html
        """
        pivot = lo
        lo += 1
        
        # 3个while循环
        while True:
            while lo <= hi and lst[hi] >= lst[pivot]:
                hi -= 1
            while lo <= hi and lst[lo] <= lst[pivot]:
                lo += 1
            if lo <= hi:
                lst[lo], lst[hi] = lst[hi], lst[lo]
            else:
                break
        # 记住这里lo和hi恰好都错位：lo指向比pivot大的元素，hi指向比pivot小的元素
        # 因此lo不用管，把hi换了就没问题了，这样hi右边恰好是比他大的元素，而左边一定是比它小的元素
        lst[pivot], lst[hi] = lst[hi], lst[pivot]
        return hi