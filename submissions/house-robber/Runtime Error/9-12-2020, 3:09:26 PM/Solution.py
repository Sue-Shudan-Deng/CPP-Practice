// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if (nums == []) return 0
        DP = [0] * len(nums)
        DP[0] = nums[0]
        DP[1] = max(nums[1], nums[0]) 
        for i in range(2, len(nums)):
            DP[i] = max(DP[i-2] + nums[i], DP[i-1])
        return DP[-1]