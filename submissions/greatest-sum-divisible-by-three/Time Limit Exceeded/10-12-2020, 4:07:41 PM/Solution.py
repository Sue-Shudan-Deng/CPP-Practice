// https://leetcode.com/problems/greatest-sum-divisible-by-three

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        Target sum + some tricks
        """
        summ = sum(nums)
        if summ % 3 == 0:
            return summ
        nums.sort()
        dp = [False for _ in range(summ + 1)]
        dp[0] = True
        for num in nums:
            for i in range(summ, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        for j in range(summ, -1, -1):
            if j % 3 == 0 and dp[j]:
                break
        return j