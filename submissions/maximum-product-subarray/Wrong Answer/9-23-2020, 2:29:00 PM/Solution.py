// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1 for _ in range(n + 1)] for _ in range(2)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n + 1):
            # dp[0][i] = max(nums[i - 1], nums[i - 1] * dp[i - 1])
            # dp[1][i] = min(nums[i - 1], nums[i])
            if nums[i-1] >= 0:
                dp[0][i] = max(nums[i-1], dp[0][i-1] * nums[i-1])
                if dp[1][i-1] != 1:
                    dp[1][i] = dp[1][i-1] * nums[i-1]
            else:
                if dp[1][i-1] != 1:
                    dp[0][i] = dp[1][i-1] * nums[i-1]
                dp[1][i] = min(nums[i-1], dp[0][i-1] * nums[i-1])
                
        # print(dp)
        part1 = dp[0][1:]
        while part1 and part1[0] == 1:
            part1.pop(0)
        part2 = dp[1][1:]
        while part2 and part2[0] == 1:
            part2.pop(0)
        return max(part1 + part2)