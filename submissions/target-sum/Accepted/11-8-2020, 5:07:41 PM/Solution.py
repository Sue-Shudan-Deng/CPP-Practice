// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        method 1: 常规解法
        https://www.youtube.com/watch?v=r6Wz4W1TbuI&t=1239s
        注意像这样的常规解法也是很重要的
        """
        n = len(nums)
        summ = sum(nums)
        if summ < S:
            return 0
         
        # 这里的offset是必要的，为了使得二维数组的第二维index合法
        offset = summ
        dp = [[0 for _ in range(2 * summ + 1)] for _ in range(n+1)]
        # dp[i][j] 表示用第i个num能达到j的情况有多少种
        dp[0][offset] = 1
        
        for i in range(1, n + 1):
            for j in range(summ + offset - nums[i-1], nums[i-1] - 1, -1):
                dp[i][j - nums[i-1]] += dp[i-1][j]
                dp[i][j + nums[i-1]] += dp[i-1][j]
                    
        return dp[n][S+offset]
    
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         """
#         method 2: bounded knapsack
#         https://www.youtube.com/watch?v=zks6mN06xdQ 重点还是理解21min的图
#         """
#         n = len(nums)
#         summ = sum(nums)
#         if summ < S or (summ + S) % 2:   # 必须被2整除
#             return 0
        
#         target = (summ + S) // 2
#         dp = [0 for _ in range(target + 1)]
#         dp[0] = 1
#         for num in nums:
#             for j in range(target, num - 1, -1):
#                 dp[j] += dp[j - num]
#         return dp[target]