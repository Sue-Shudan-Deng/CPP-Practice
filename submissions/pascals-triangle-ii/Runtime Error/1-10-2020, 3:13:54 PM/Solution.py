// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1 for i in range(numRows)]
        if numRows <= 2:
            return ans
        for i in range(2, numRows):
            for j in range(1, len(ans[i]) - 1):
                ans[j] = ans[j-1] + ans[j]
        return ans