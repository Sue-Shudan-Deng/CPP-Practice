// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2 = sorted(list(map(abs, nums)))
        
        squared = (i**2 for i in nums2)
        
        return squared