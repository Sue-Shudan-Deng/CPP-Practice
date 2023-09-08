// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[float("inf") for _ in range(2)] for _ in range(n)]
        # dp[i][0] keep i
        # dp[i-1][0] swap i-1
        
        dp[0][0] = 0 # 因为第一个无论是谁总是可以不换的 
        dp[0][1] = 1 # 因为第一个无论是谁总是可以交换的
        
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp[i][0] = dp[i-1][0]     # 保持
                dp[i][1] = dp[i-1][1] + 1 # 换回来 
                
            if B[i] > A[i-1] and A[i] > B[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][1]) 
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)
                
        return min(dp[-1])