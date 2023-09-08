// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        ans = 0
        # 只要l_max < r_max, 计算左边时那么就一定不用担心右边会没人给拦着
        # 同理，只要r_max < l_max, 计算右边时就不用担心左边没人给拦着
        while l < r:
            if height[l] > l_max:
                l_max = height[l]
            if height[r] > r_max:
                r_max = height[r]
            if l_max < r_max:
                # 放心计算左边
                ans += max(0, l_max - height[l])
                l += 1
            else:
                # 放心计算右边
                ans += max(0, r_max - height[r])
                r -= 1
        return ans