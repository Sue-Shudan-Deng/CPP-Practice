// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Unbounded knapsack with combination duplicates
        """
        if not nums or min(nums) > target:
            return 0
        dp = [1 for _ in range(target + 1)]
        dp[0] = 0
        for num in nums:
            for i in range(num, target + 1):
                dp[i] += dp[i - num]
        return dp[target]