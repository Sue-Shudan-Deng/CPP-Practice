// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return max(nums[0], nums[1])
        
        # case 1: rob at index 0
        dp1 = [0 for _ in range(n-1)]
        dp1[0] = nums[0]
        dp1[1] = nums[0]
        
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            
        # case 2: don't rob at index 0
        dp2 = [0 for _ in range(n)]
        dp2[0] = 0
        dp2[1] = nums[1]
        
        for i in range(2, n):
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
                
        return max(dp2[-1], dp1[-1])