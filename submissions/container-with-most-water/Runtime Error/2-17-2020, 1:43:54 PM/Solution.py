// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height)
        l = 0
        res = 0
        while (l < r):
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1
        return res