// https://leetcode.com/problems/maximal-rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        build histgram + max rectangle in histgram (84)
        """
        def build_hist(r, dp):
            for c in range(col):
                if matrix[r-1][c] == "0":
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + 1
        
        def maxRectInHist(hist):
            n, ans = len(hist), 0
            stack = [-1]
            
            for i in range(n):
                while stack[-1] != -1 and hist[i] < hist[stack[-1]]:
                    index = stack.pop()
                    ans = max(ans, hist[index] * (i - stack[-1] - 1))
                stack.append(i)
            
            while stack[-1] != -1:
                index = stack.pop()
                ans = max(ans, hist[index] * (n - stack[-1] - 1))
            
            return ans
        
        if not matrix or len(matrix) == 0:
            return 0
        row, col, ans = len(matrix), len(matrix[0]), 0
        dp = [[0 for _ in range(col)] for _ in range(row + 1)]
        for r in range(row):
            build_hist(r, dp)
            ans = max(ans, maxRectInHist(dp[r]))
            
        return ans