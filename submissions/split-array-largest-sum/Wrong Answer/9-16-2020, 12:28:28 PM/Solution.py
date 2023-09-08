// https://leetcode.com/problems/split-array-largest-sum

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        nums = [i for i in nums if i != 0]
        dp = [[float("inf") for j in range(m+1)] for i in range(len(nums)+1)]
        summ = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            summ[i] = summ[i-1] + nums[i-1]
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            for j in range(1, m+1):
                for k in range(0, i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], (summ[i]-summ[k])))
        return dp[-1][-1]