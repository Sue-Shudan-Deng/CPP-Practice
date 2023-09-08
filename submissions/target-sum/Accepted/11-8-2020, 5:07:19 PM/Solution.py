// https://leetcode.com/problems/target-sum

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        写一遍常规解法
        """
        summ, n = sum(nums), len(nums)
        offset = summ
        if summ < S:
            return 0
        dp = [[0 for _ in range(summ + offset + 1)] for _ in range(n + 1)]
        dp[0][offset] = 1
        
        for i in range(1, n + 1):
            for j in range(summ + offset - nums[i-1], nums[i-1] - 1, -1):
                dp[i][j - nums[i-1]] += dp[i-1][j]
                dp[i][j + nums[i-1]] += dp[i-1][j]
        
        return dp[n][offset + S]
        