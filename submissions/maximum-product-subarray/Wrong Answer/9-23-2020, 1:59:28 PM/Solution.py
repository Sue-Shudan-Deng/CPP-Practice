// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = max(nums[i - 1], nums[i - 1] * dp[i - 1])
        return max(dp[1:])