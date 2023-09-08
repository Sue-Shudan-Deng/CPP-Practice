// https://leetcode.com/problems/stone-game-ii

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=e_FrC5xavwI
        Recursion with mem
        """
        n = len(piles)
        dp = [[0 for _ in range(n + 1)] for _ in range(n)]
        def dfs(i, M):
            if i >= n:
                return 0
            M = min(M, n)
            if i + 2 * M >= n:
                dp[i][M] = sum(piles[i:])
                return dp[i][M]
            # make sure i + 2 * M < n
            tmp, curr = float("-inf"), 0
            for x in range(1, 2 * M + 1):
                curr += piles[i + x - 1]
                tmp = max(tmp, curr - dfs(i+x, max(M, x)))
            dp[i][M] = tmp
            return tmp
        return (sum(piles) + dfs(0, 1)) // 2