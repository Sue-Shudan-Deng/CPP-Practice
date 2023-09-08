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
        n, step, l, r, new_r = len(nums), 0, 0, 0, 0
        # 如果初始已包含终点，返回0
        if nums[0] == 0 or len(nums) == 1:
            return 0
        # 否则，至少+1
        while l <= r:
            for i in range(l, r + 1):
                new_r = max(new_r, i + nums[i])
                if new_r >= n - 1:
                    return step + 1
            l = r + 1
            r = new_r
            step += 1
        return step