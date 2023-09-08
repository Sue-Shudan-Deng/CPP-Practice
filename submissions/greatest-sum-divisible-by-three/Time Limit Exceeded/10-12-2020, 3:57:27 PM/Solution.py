// https://leetcode.com/problems/greatest-sum-divisible-by-three

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        Target sum + some trick
        """
        summ = sum(nums)
        if summ % 3 == 0:
            return summ
        divisable_list = []
        for n in nums:
            if n % 3 == 0:
                divisable_list.append(n)
        summ -= sum(divisable_list)
        dp = [False for _ in range(summ + 1)]
        dp[0] = True
        for num in nums:
            if num in divisable_list:
                continue
            for i in range(summ, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        for j in range(summ, -1, -1):
            if j % 3 == 0 and dp[j]:
                break
        return j + sum(divisable_list)