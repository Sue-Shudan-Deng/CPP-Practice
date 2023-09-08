// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        ans = 0
        while l <= r:
            if height[l] < height[r]:
                if height[l] < l_max:
                    ans += (l_max - height[l])
                else:
                    l_max = height[l]
                l += 1
            else:
                if height[r] < r_max:
                    ans += (r_max - height[r])
                else:
                    r_max = height[r]
                r -= 1
        return ans