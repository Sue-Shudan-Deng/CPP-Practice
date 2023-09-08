// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        ans = 0
        while l <= r:
            if l == r:
                ans += min(l_max, r_max) - height[l]
            while height[l] < l_max:
                ans += (l_max - height[l])
                l += 1
            while height[r] < r_max:
                ans += (r_max - height[r])
                r -= 1
            if height[l] >= l_max:
                l_max = height[l]
                l += 1
            if height[r] >= r_max:
                r_max = height[r]
                r -= 1
        return ans