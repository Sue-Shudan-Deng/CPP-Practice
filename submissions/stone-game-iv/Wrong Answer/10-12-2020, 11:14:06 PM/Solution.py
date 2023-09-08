// https://leetcode.com/problems/stone-game-iv

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        def dfs(i, parity):
            if i == 0:
                return True if not parity else False
            tmp = True
            for x in range(1, int(i ** 0.5)  + 1):
                tmp = tmp and dfs(i - x ** 2, not parity)
            return tmp
        
        return dfs(n, True)