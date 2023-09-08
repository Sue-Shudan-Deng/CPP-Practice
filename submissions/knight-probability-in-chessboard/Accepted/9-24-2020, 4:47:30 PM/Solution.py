// https://leetcode.com/problems/knight-probability-in-chessboard

class Solution:
    def knightProbability(self, N: int, K: int, i: int, j: int) -> float:
        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]
        """
        dp[s][r][c] 记录从r, c开始，走s步出界
        """
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        dp[0][i][j] = 1
        for s in range(1, K + 1):
            for r in range(N):
                for c in range(N):
                    for dr, dc in dirs:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < N and 0 <= new_c < N:
                            dp[s][r][c] += dp[s-1][new_r][new_c]
                
        total = 0
        for i in range(N):
            for j in range(N):
                total += dp[K][i][j]
        return total * (1/8) ** K