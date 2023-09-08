// https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for left in range(len(nums)-2, -1, -1):
            for right in range(left+2, len(nums), 1):
                dp[left][right] = max([dp[left][k] + nums[left]*nums[k]*nums[right] + dp[k][right] for k in range(left+1, right)])
        print(dp)
        return dp[0][-1]