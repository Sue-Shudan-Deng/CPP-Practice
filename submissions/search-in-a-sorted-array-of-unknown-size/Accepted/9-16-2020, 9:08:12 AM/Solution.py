// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, r = 0, 10000
        while l < r:
            m = l + (r - l) // 2
            if target <= reader.get(m):
                r = m
            else:
                l = m + 1
        if reader.get(l) == target:
            return l
        else:
            return -1