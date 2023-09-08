// https://leetcode.com/problems/stone-game-iii

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # """
        # method 1: 我自己的思路，函数是以后手的角度进行写的
        # """
        # n = len(stoneValue)
        # dp = [[0 for _ in range(4)] for _ in range(n)]
        # def dfs(i, M):
        #     if i >= n:
        #         return 0
        #     if dp[i][M]:
        #         return dp[i][M]
        #     tmp, cur = float("inf"), sum(stoneValue[i:i+M])
        #     for x in range(1, 4):
        #         tmp = min(tmp, cur - dfs(i+M, x))
        #     dp[i][M] = tmp
        #     return tmp
        # score = max(dfs(0,1), dfs(0,2), dfs(0,3))
        # if score > 0:
        #     return "Alice"
        # elif score < 0:
        #     return "Bob"
        # else:
        #     return "Tie"
        """
        method 2: hua hua
        """
        n = len(stoneValue)
        dp = [0 for _ in range(n)]
        
        def dfs(i):
            if i >= n:
                return 0
            if dp[i]:
                return dp[i]
            tmp, cur = float("-inf"), 0
            for x in range(1, 4):
                if i + x <= n:
                    cur += stoneValue[i+x-1]
                    tmp = max(tmp, cur - dfs(i+x))
            dp[i] = tmp
            return tmp
        
        score = dfs(0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"