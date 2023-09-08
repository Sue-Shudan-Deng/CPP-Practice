// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        nums = []
        while i**2 <= x:
            nums.append(i)
            i += 1
        nums = list(range(x+1))
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m]**2 <= x and nums[m+1]**2 > x:
                return nums[m]
            elif nums[m+1]**2 <= x:
                r = m-1
            else:
                l = m+1