// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Unbounded knapsack
        """
        if not nums or min(nums) > target:
            return 0
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]