// https://leetcode.com/problems/partition-array-for-maximum-sum

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], K: int) -> int:
        """
        https://www.youtube.com/watch?v=3M8q-wB2tmw
        其实思路很简单
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