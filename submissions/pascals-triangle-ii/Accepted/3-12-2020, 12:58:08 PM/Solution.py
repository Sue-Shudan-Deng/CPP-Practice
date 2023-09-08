// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1 for _ in range(rowIndex + 1)]
        for lvl in range(rowIndex - 1):
            for i in range(lvl, -1, -1):
                res[i + 1] += res[i]
        return res