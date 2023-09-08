// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """
        这道题是2道题的结合：prefix_sum, best buy and sell III
        """
        n, K = len(A), 2
        prefix = [0 for _ in range(n+1)]
        for i in range(1, len(A)+1):
            prefix[i] = prefix[i-1] + A[i-1]
        dp = [0 for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i] = max(dp[i], dp[i-1])
            if i >= L:
                dp[i] = max(dp[i], prefix[i] - prefix[i-L])
        for i in range(1, n+1):
            dp[i] = max(dp[i], dp[i-1])
            if i > M:
                dp[i] = max(dp[i], dp[i-M-1] + prefix[i] - prefix[i-M])
        return dp[-1]