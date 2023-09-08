// https://leetcode.com/problems/stone-game

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dfs(i, j):
            if i > j:
                return 0
            parity = (j - i - len(piles)) % 2
            if parity == 1:
                return max(piles[i] + dfs(i + 1, j), piles[j] + dfs(i, j - 1))
            else:
                return min(-piles[i] + dfs(i + 1, j), -piles[j] + dfs(i, j - 1))
            
        return dfs(0, len(piles) - 1) > 0