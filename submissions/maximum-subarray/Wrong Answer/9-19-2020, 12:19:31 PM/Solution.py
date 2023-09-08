// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP
        """
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = max(dp[i-1], dp[i-1] + nums[i-1])
        return dp[-1]