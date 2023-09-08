// https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        """
        注意这里left的次序非常重要！！
        """
        
        for left in range(n-3, -1, -1):
            for right in range(left+2, n, 1):
                dp[left][right] = max([dp[left][k] + nums[left]*nums[k]*nums[right] + dp[k][right] for k in range(left+1, right)])
        return dp[0][-1]