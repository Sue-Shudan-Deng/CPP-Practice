// https://leetcode.com/problems/remove-boxes

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=wT7aS5fHZhs
        """
        n = len(boxes)
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        # dp[i][j][k], b[j]后面有k个和b[j]的值相同的data point
        def dfs(i, j, k):
            if i > j:
                return 0
            if dp[i][j][k]:
                return dp[i][j][k]
            dp[i][j][k] = dfs(i,j-1,0) + (k+1) ** 2
            for p in range(i, j):
                if boxes[p] == boxes[j]:
                    dp[i][j][k] = max(dp[i][j][k], dfs(i,p,k+1) + dfs(p+1,j-1,0))
            return dp[i][j][k]                
        return dfs(0, n - 1, 0)
                