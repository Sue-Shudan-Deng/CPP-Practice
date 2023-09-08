// https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        """
        注意这里l的次序非常重要！！一定是要从最后开始！！否则不满足无后效性
        """
        for l in range(n-3, -1, -1):
            for r in range(l+2, n, 1):
                dp[l][r] = max([dp[l][k] + nums[l]*nums[k]*nums[r] + dp[k][r] for k in range(l+1, r)])
        return dp[0][-1]