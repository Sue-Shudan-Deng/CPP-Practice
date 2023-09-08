// https://leetcode.com/problems/stone-game

from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        DP, minmax
        """
        n = len(piles)
        
        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            parity = (j - i - n) % 2
            if parity == 1:
                return max(piles[i] + dfs(i + 1, j), piles[j] + dfs(i, j - 1))
            else:
                return min(-piles[i] + dfs(i + 1, j), -piles[j] + dfs(i, j - 1))
            
        return dfs(0, n - 1) > 0