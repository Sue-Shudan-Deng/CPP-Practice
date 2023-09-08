// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        DP, O(n^2)
        """
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        for i in range(n-1, -1, -1):
            if i + nums[i] >= n:
                dp[i] = 0
            elif nums[i] > 0:
                for j in range(i + 1, i + nums[i] + 1):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]