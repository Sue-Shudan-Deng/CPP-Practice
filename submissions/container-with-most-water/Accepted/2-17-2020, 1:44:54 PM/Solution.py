// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) - 1
        l = 0
        res = 0
        while (l < r):
            res = max(res, min(height[l], height[r]) * (r - l))
            if (height[l] <= height[r]):
                l += 1
            else:
                r -= 1
        return res