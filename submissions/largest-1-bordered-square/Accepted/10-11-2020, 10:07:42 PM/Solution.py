// https://leetcode.com/problems/largest-1-bordered-square

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=7IkOZOwc-Mc&t=58s, 
        其实类似于matrix square的method 1, 属于brute force + dp, O(n^3)
        """
        if not grid or len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        dp = [[[0 for _ in range(2)] for _ in range(col+1)] for _ in range(row+1)]
        # dp[i][j][0]: number of consecutive 1 from i,j to left
        # dp[i][j][1]: number of consecutive 1 from i,j to top
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                if grid[r-1][c-1]:
                    dp[r][c][0] = dp[r][c-1][0] + 1
                    dp[r][c][1] = dp[r-1][c][1] + 1
        ans = 0
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                if grid[r-1][c-1]:
                    size = min(dp[r][c][0], dp[r][c][1])
                    for k in range(size, 0, -1):
                        p = min(dp[r-k+1][c][0], dp[r][c-k+1][1])
                        if p >= k:
                            ans = max(ans, k ** 2)
                            break
        return ans