// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        method 1: move backward, DP, O(n^2), TLE
        """
        # n = len(nums)
        # dp = [float("inf") for _ in range(n)]
        # dp[-1] = 0
        # for i in range(n-2, -1, -1):
        #     if i + nums[i] >= n:
        #         dp[i] = 1
        #     elif nums[i] > 0:
        #         for j in range(i + 1, i + nums[i] + 1):
        #             dp[i] = min(dp[i], dp[j] + 1)
        # return 0 if dp[0] == float("inf") else dp[0]
    
        """
        method 2: move forard, Greedy
        """
        n, farthest, steps, last = len(nums), 0, 0, -1
        if nums[0] == 0:
            return 0
        for i in range(n):
            farthest = max(farthest, i + nums[i])
            if i > last:
                last = farthest
                steps += 1
        return steps