// https://leetcode.com/problems/out-of-boundary-paths

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N+1)]
        
        """
        https://www.youtube.com/watch?v=92zh6XvqEgc
        dp[s][r][c] 表示从边界外走多少步可以到[r, c]，等价于从r, c开始走有多少种办法可以出界
        """
        mod = (10 ** 9 + 7)
        dirs = [-1, 0, 1, 0, -1]
        for s in range(1, N + 1):
            for r in range(m):
                for c in range(n):
                    for d in range(4):
                        new_r, new_c = r + dirs[d], c + dirs[d+1]
                        # """
                        # 下面的写法太巧妙
                        # 本质是 1 -> 2, 1 -> 3, 2, 1 -> 4, 3, 2, 1
                        # 最后 4 + 3 + 2 + 1
                        # """
                        # if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n:
                        #     dp[s][r][c] += 1
                        # else:
                        #     dp[s][r][c] = (dp[s][r][c] + dp[s-1][new_r][new_c]) % mod
                            
                        """
                        写法2：naive版
                        """
                        if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n:
                            if s == 1:
                                dp[s][r][c] += 1
                        else:
                            dp[s][r][c] = (dp[s][r][c] + dp[s-1][new_r][new_c])
                            
        return sum(dp[s][i][j] for s in range(1, N + 1))