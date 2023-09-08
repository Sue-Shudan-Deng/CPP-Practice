// https://leetcode.com/problems/jump-game

class Solution:
    """
    Solution 1: DP, TLE, O(n^2)
    """
    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     dp = [False for _ in range(n)]
    #     dp[-1] = True
    #     for i in range(n-2, -1, -1):
    #         for j in range(i+1, i+nums[i]+1):
    #             if j >= n or dp[j]:
    #                 dp[i] = True
    #                 break
    #     return dp[0]
    """
    Solution 2: Greedy, O(n)
    we only need to keep track of the furthest achievable element
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastpoint = n-1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= lastpoint:
                lastpoint = i
        return lastpoint == 0