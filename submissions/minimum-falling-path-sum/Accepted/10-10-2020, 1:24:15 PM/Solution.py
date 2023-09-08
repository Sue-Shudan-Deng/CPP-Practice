// https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0]) 
        dp = [[float("inf") for _ in range(col + 2)] for _ in range(row + 2)]
        dp[-1] = [0 for _ in range(col + 2)]
        for r in range(row, 0, -1):
            for c in range(col, 0, -1):
                dp[r][c] = A[r-1][c-1] + min(dp[r+1][c+1], dp[r+1][c], dp[r+1][c-1])
        return min(dp[1])