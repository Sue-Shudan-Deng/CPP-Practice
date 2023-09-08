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
        l, r = -2**31, 2**31-1
        while l < r:
            m, c = l + (r - l) // 2, 0
            for num in nums:
                if num >= m:
                    c += 1
            if c <= k:
                r = m
            else:
                l = m + 1
        return l