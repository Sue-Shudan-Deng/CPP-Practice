// https://leetcode.com/problems/maximum-length-of-repeated-subarray

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        nA, nB = len(A), len(B)
        dp = [[0 for _ in range(nB + 1)] for _ in range(nA + 1)]
        for i in range(1, nA + 1):
            for j in range(1, nB + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        return max(max(dp))