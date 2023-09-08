// https://leetcode.com/problems/partition-array-for-maximum-sum

class Solution(object):
    def maxSumAfterPartitioning(self, arr, K):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            m = 0
            for k in range (1, min(K, i) + 1):
                m = max(m, arr[i-k])
                dp[i] = max(dp[i], dp[i-k] + m * k)
                
        return dp[-1]