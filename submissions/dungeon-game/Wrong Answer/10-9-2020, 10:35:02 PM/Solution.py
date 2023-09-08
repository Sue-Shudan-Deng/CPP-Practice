// https://leetcode.com/problems/dungeon-game

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        dp0 = [[float("-inf") for _ in range(col + 1)] for _ in range(row + 1)]
        dp1 = [[float("-inf") for _ in range(col + 1)] for _ in range(row + 1)]
        # dp0[i][j] # current normal value
        # dp1[i][j] # current met min value
        
        if dungeon == []:
            return 1
        dp0[0][1], dp0[1][0], dp1[0][1], dp1[1][0] = 0, 0, 0, 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp0[i][j] = dungeon[i-1][j-1] + max(dp0[i-1][j], dp0[i][j-1])
                if dp0[i-1][j] < 0 and dp0[i][j-1] < 0:
                    tmp0 = max(dp0[i-1][j], dp0[i][j-1])
                else:
                    tmp0 = min(dp0[i-1][j], dp0[i][j-1])
                    if tmp0 == float("-inf"):
                        tmp0 = dp0[i-1][j] if dp0[i][j-1] == float("-inf") else dp0[i][j-1]
                tmp1 = max(dp1[i-1][j], dp1[i][j-1])
                dp1[i][j] = min(tmp1, tmp0 + dungeon[i-1][j-1])
        return -dp1[-1][-1] + 1