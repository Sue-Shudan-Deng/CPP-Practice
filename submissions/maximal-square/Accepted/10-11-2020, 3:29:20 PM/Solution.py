// https://leetcode.com/problems/maximal-square

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        method 1: brute-force with dp, https://www.youtube.com/watch?v=vkFUB--OYy0
        """
        # Step1: use dp to memorize the intergral image
        if matrix == []:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + int(matrix[r-1][c-1])
        # Step2: check if the current area is such a square
        ans = 0
        for r in range(row + 1):
            for c in range(col + 1):
                # for all possible sizes
                for k in range(min(row - r, col - c), 0, -1):
                    acc = dp[r+k][c+k] - dp[r][c+k] - dp[r+k][c] + dp[r][c]
                    if acc == k ** 2:
                        ans = max(ans, acc)
                        break
        return ans