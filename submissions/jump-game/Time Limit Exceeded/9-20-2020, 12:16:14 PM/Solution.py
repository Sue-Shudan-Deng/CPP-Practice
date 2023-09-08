// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[-1] = True
        if nums[0] >= n -1:
            return True
        for i in range(n-2, -1, -1):
            for j in range(nums[i], -1, -1):
                if i + j >= n or dp[i+j]:
                    dp[i] = True
                    break
        return dp[0]