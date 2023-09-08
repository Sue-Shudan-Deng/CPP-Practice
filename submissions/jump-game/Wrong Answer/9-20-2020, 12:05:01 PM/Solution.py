// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[-1] = True
        for i in range(n-2, -1, -1):
            if i + nums[i] < n:
                dp[i] = dp[i + nums[i]]
            else:
                dp[i] = True
        return dp[0]