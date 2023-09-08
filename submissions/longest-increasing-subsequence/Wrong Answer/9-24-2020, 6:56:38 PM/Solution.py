// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        method 1: DP: O(n^2)
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)