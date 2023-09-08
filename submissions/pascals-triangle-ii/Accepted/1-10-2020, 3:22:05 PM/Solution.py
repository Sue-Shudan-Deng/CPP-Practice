// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1 for i in range(rowIndex+1)]
        if rowIndex <= 1:
            return ans
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                ans[j] = ans[j-1] + ans[j]
        return ans