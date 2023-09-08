// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        method 1: DP: O(n^2)
        """
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i):
                if nums[j-1] < nums[i-1]:
                    dp[i] = max(dp[j], dp[i])
            dp[i] += 1
        return max(dp[1:])