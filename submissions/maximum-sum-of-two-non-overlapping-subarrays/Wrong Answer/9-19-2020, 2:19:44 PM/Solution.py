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
        dp = [[0 for _ in range(n+1)] for _ in range(K)]
        
        # L is before M
        
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1]
            if i >= L:
                dp[0][i] = max(dp[0][i], prefix[i] - prefix[i-L])
                
        for i in range(1, n+1):
            dp[1][i] = dp[1][i-1]
            if i > M:
                dp[1][i] = max(dp[1][i], dp[0][i-M-1] + prefix[i] - prefix[i-M])
        res1 = dp[1][-1]
        # M is before L
        dp = [[0 for _ in range(n+1)] for _ in range(K)]
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1]
            if i >= M:
                dp[0][i] = max(dp[0][i], prefix[i] - prefix[i-M])
                
        for i in range(1, n+1):
            dp[1][i] = dp[1][i-1]
            if i > L:
                dp[1][i] = max(dp[1][i], dp[0][i-L-1] + prefix[i] - prefix[i-L])
        res2 = dp[1][-1]
        return max(res1, res2)