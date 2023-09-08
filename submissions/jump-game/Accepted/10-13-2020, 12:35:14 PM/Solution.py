// https://leetcode.com/problems/jump-game

class Solution:
    """
    method 1: move backward, DP, TLE, O(n^2)
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
    method 2: move backward, Greedy, O(n)
    we only need to keep track of the furthest achievable element
    """
    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     lastpoint = n-1
    #     for i in range(n-2, -1, -1):
    #         if i + nums[i] >= lastpoint:
    #             lastpoint = i
    #     return lastpoint == 0
    
    """
    method 3: move forward, Greedy, O(n)
    https://www.youtube.com/watch?v=J04GagAZ5io
    核心思想是每步都更新右边界，看最远能到达哪里
    """
    # def canJump(self, nums: List[int]) -> bool:
    #     n, farthest = len(nums), 0
    #     for i in range(n):
    #         if i > farthest:
    #             return False
    #         farthest = max(farthest, i + nums[i])
    #     return True
    """
    method 4: move forard, Greedy, another version
    """
    def canJump(self, nums: List[int]) -> bool:
        n, l, r, new_r = len(nums), 0, 0, 0
        # 如果初始已包含终点，返回0
        # 否则，至少+1
        while l <= r:
            for i in range(l, r + 1):
                new_r = max(new_r, i + nums[i])
                if new_r >= n - 1:
                    return True
            l = r + 1
            r = new_r
        return False