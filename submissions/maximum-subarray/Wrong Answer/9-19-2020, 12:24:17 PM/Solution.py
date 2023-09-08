// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP
        """
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            # 用不用之前的数组？用，第一个; 不用，第二个
            dp[i] = max(dp[i-1] + nums[i-1], nums[i-1])
        return max(dp)