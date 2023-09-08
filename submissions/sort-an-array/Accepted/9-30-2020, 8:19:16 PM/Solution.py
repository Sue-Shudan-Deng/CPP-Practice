// https://leetcode.com/problems/sort-an-array

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         """
#         Counting sort, O(1)
#         """
#         C, m, M, S = collections.Counter(nums), min(nums), max(nums), []
#         for n in range(m, M+1):
#             S.extend([n]*C[n])
#         return S
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Bottom-up mergesort
        """
        def merge(l1: List[int], l2: List[int]) -> List[int]:
            res = []
            left_cursor = 0
            right_cursor = 0
            while left_cursor < len(l1) and right_cursor < len(l2):
                if l1[left_cursor] < l2[right_cursor]:
                    res.append(l1[left_cursor])
                    left_cursor += 1
                else:
                    res.append(l2[right_cursor])
                    right_cursor += 1
            res.extend(l1[left_cursor:])
            res.extend(l2[right_cursor:])
            return res
            
        size = 1
        while size < len(nums):
            for i in range(0, len(nums)-size, size*2):  # 这一步的想法是关键
                nums[i:i+size*2] = merge(nums[i:i+size], nums[i+size:i+2*size])
            size *= 2
        return nums
              
# class Solution:        
#     def sortArray(self, nums: List[int]) -> List[int]:
#         """
#         quick sort
#         """
#         self.qsort(nums, 0, len(nums)-1) # 一定要注意，python是按引用传递的，不是按值传递，因此nums的值会修改
#         return nums

#     def qsort(self, lst, lo, hi):
#         if lo < hi:
#             p = self.partition(lst, lo, hi)
#             self.qsort(lst, lo, p - 1)
#             self.qsort(lst, p + 1, hi)
    
#     def partition(self, lst, lo, hi):
#         """
#         简单双向版本，pivot取lo
#         实践证明面试一定不要尝试三数取中法，edge case太麻烦
#         http://www.cs.armstrong.edu/liang/animation/web/QuickSortPartition.html
#         """
#         pivot = lo
#         lo += 1
        
#         # 3个while循环
#         while True:
#             while lo <= hi and lst[hi] >= lst[pivot]:
#                 hi -= 1
#             while lo <= hi and lst[lo] <= lst[pivot]:
#                 lo += 1
#             if lo <= hi:
#                 lst[lo], lst[hi] = lst[hi], lst[lo]
#             else:
#                 break
#         # 记住这里lo和hi恰好都错位：lo指向比pivot大的元素，hi指向比pivot小的元素
#         # 因此lo不用管，把hi换了就没问题了，这样hi右边恰好是比他大的元素，而左边一定是比它小的元素
#         lst[pivot], lst[hi] = lst[hi], lst[pivot]
#         return hi