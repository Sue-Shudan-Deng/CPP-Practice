// https://leetcode.com/problems/stone-game-iv

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = dict()
        def dfs(i, parity):
            if i == 0:
                return True if not parity else False
            if (i, parity) in dp:
                return dp[(i, parity)]
            if parity:
                tmp = False
                for x in range(1, int(i ** 0.5)  + 1):
                    tmp = tmp or dfs(i - x ** 2, 0)
            else:
                tmp = True
                for x in range(1, int(i ** 0.5)  + 1):
                    tmp = tmp and dfs(i - x ** 2, 1)
            dp[(i, parity)] = tmp
            return tmp
        return dfs(n, 1)