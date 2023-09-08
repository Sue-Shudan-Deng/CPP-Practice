// https://leetcode.com/problems/cherry-pickup

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=vvPSWORCKow&t=641s
        难点1: 往返走两次相当于两个人以一个方向走一次
        难点2: 同时走可以节省一个复杂度
        """
        n = len(grid)
        dp = [[[float("-inf") for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
        dp[1][1][1] = float("-inf") if grid[0][0] == -1 else grid[0][0]
        # dp[x1][x2][y1]: (x1, y1), (x2, y2) 时走到(N-1, N-1) 最多的cherry是多少
        # y2 = x1 + y1 - x2
        for x1 in range(1, n + 1):
            for y1 in range(1, n + 1):
                if x1 == 1 and y1 == 1:
                    continue
                if grid[x1-1][y1-1] == -1:
                    continue
                for x2 in range(max(1, x1 + y1 - n), min(x1 + y1, n + 1)):
                    y2 = x1 + y1 - x2
                    if grid[x2-1][y2-1] == -1:
                        continue
                    dp[x1][y1][x2] = grid[x1-1][y1-1] + grid[x2-1][y2-1] - (x1 == x2 and y1 == y2 and grid[x1-1][y1-1]) + max(dp[x1-1][y1][x2-1], dp[x1-1][y1][x2], dp[x1][y1-1][x2-1], dp[x1][y1-1][x2])
        
        return dp[-1][-1][-1] if dp[-1][-1][-1] != float("-inf") else 0