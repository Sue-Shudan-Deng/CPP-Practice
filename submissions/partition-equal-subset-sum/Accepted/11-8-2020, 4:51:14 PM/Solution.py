// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2:
            return False
        target = summ // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[target]
        