// https://leetcode.com/problems/stone-game-iii

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[0 for _ in range(4)] for _ in range(n)]
        def dfs(i, M):
            if i >= n:
                return 0
            if dp[i][M]:
                return dp[i][M]
            # make sure i + 2 * M < n
            tmp, cur = float("inf"), sum(stoneValue[i:i+M])
            for x in range(1, 4):
                tmp = min(tmp, cur - dfs(i+M, x))
            dp[i][M] = tmp
            return tmp
        score = max(dfs(0,1), dfs(0,2), dfs(0,3))
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"