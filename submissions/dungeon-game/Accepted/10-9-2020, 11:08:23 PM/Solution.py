// https://leetcode.com/problems/dungeon-game

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        
        # hp: min hp needed to go from [r-1][c-1] to [r][c]
        hp = [[float("inf") for _ in range(col + 1)] for _ in range(row + 1)]
        hp[row][col-1], hp[row-1][col] = 1, 1
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                hp[r][c] = max(1, min(hp[r+1][c], hp[r][c+1]) - dungeon[r][c])
        return hp[0][0]