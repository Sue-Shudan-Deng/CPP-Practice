// https://leetcode.com/problems/partition-array-for-maximum-sum

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], K: int) -> int:
        """
        思路和 Best time to buy and sell stock 相似
        """
        n = len(arr)
        dp = [0 for _ in range(n + 1)]
        # dp[i] = 
        for i in range(1, n + 1):
            m = 0
            for k in range(1, min(K, i) + 1):
                m = max(m, arr[i-k])
                dp[i] = max(dp[i], dp[i-k] + m * k)
        return max(dp)